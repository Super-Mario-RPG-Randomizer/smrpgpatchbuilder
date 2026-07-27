#!/usr/bin/env python3
"""Extract repeated sequences from the analyzer report into subroutines.

Usage:
    python scripts/extract_sequence.py <seq_num>
    python scripts/extract_sequence.py --loop [--max N]

Single mode:
    Extracts one sequence identified by its number in the current report.

Loop mode:
    Runs analyze_repeated_sequences.py → picks the top bank 0x35 sequence with
    savings > 0 → extracts → runs the animationassembler. On assembler failure
    or any safety check failure, aborts immediately so the user can recover.

Safety checks:
    Every target index is verified against the expected command-class list
    parsed from the report before any file is modified. A mismatch (stale
    report, already-extracted region, etc.) aborts loudly rather than silently
    corrupting.

Picks the FIRST occurrence as source-of-truth. For every command position
whose source has no identifier but a non-source occurrence does, gives the
source a UUID identifier and renames the non-source identifier globally within
bank 0x35 to match. Replaces each non-source occurrence with a single Jmp to
the source's first-command identifier.

Bank 0x35 only.
"""

import argparse
import re
import subprocess
import sys
import uuid
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = REPO_ROOT / "scripts" / "repeated_sequences_report.txt"
ANALYZER = REPO_ROOT / "scripts" / "analyze_repeated_sequences.py"
MANAGE_PY = REPO_ROOT / "src" / "smrpgpatchbuilder" / "manage.py"
PYTHON = REPO_ROOT / "patchvenv" / "bin" / "python"

# Mutable globals configured by main() based on --bank.
BANK_PATH: Path = REPO_ROOT / "src" / "disassembler_output" / "battle_animation" / "35" / "contents"
BANK_LABEL: str = "0x35"


def configure_bank(bank_dir: str) -> None:
    """Point BANK_PATH/BANK_LABEL at a bank directory like '35', '3A', or '02'."""
    global BANK_PATH, BANK_LABEL
    BANK_PATH = (
        REPO_ROOT / "src" / "disassembler_output" / "battle_animation" / bank_dir / "contents"
    )
    BANK_LABEL = f"0x{bank_dir.upper()}"
    if not BANK_PATH.is_dir():
        sys.exit(f"bank dir not found: {BANK_PATH}")

LINE_BASE = 15  # 0-based list index of the first command (line 16 in 1-based)
IDENT_RE = re.compile(r'\bidentifier\s*=\s*"([^"]+)"')
CLASS_RE = re.compile(r"^\s*(\w+)\s*\(")


def parse_report(report_path: Path) -> dict[int, dict]:
    """Parse the report into a dict of sequence_number -> metadata."""
    text = report_path.read_text()
    sequences: dict[int, dict] = {}
    blocks = re.split(r"^SEQUENCE #", text, flags=re.MULTILINE)[1:]
    for block in blocks:
        m_num = re.match(r"(\d+)", block)
        if not m_num:
            continue
        num = int(m_num.group(1))
        m_bank = re.search(r"^Bank: (\S+)", block, re.MULTILINE)
        m_len = re.search(r"^Length: (\d+)", block, re.MULTILINE)
        m_sav = re.search(r"^Potential savings: ~(\d+)", block, re.MULTILINE)
        if not (m_bank and m_len):
            continue
        # Commands block: "  N. ClassName(...)"
        cmd_section = re.search(r"^Commands:\n((?:\s+\d+\..+\n)+)", block, re.MULTILINE)
        expected_classes: list[str] = []
        if cmd_section:
            for line in cmd_section.group(1).splitlines():
                m = re.match(r"\s+\d+\.\s+(\w+)\s*\(", line)
                if m:
                    expected_classes.append(m.group(1))
        locs = [(f, int(i)) for f, i in re.findall(r"- (\S+\.py) at index (\d+)", block)]
        sequences[num] = {
            "bank": m_bank.group(1),
            "length": int(m_len.group(1)),
            "savings": int(m_sav.group(1)) if m_sav else 0,
            "expected_classes": expected_classes,
            "locations": locs,
        }
    return sequences


def set_identifier(line: str, ident: str) -> str:
    """Replace or insert an identifier=\"...\" kwarg on a command line."""
    has_nl = line.endswith("\n")
    body = line.rstrip("\n")

    if IDENT_RE.search(body):
        body = IDENT_RE.sub(f'identifier="{ident}"', body)
    else:
        m = re.match(r"^(\s*)(\w+)\((.*)\)(,?\s*)$", body, re.DOTALL)
        if not m:
            raise ValueError(f"could not parse command line: {body!r}")
        indent, cls, args, tail = m.groups()
        args = args.rstrip()
        new_args = f'{args}, identifier="{ident}"' if args.strip() else f'identifier="{ident}"'
        body = f"{indent}{cls}({new_args}){tail}"

    return body + ("\n" if has_nl else "")


def line_class(line: str) -> str | None:
    m = CLASS_RE.match(line)
    return m.group(1) if m else None


DEF_RE = re.compile(r'\bidentifier\s*=\s*"([^"]+)"')
STR_RE = re.compile(r'"([^"]+)"')


def validate_identifier_graph(files: dict[str, list[str]]) -> None:
    """Abort (SkipSequence) if any destination reference lacks a definition.

    Every `identifier="X"` is a definition. Every other quoted string is a
    reference. Referenced names without a matching definition mean an earlier
    step deleted the definition without redirecting its references — aborting
    here prevents writing files that the assembler will reject.
    """
    defs: set[str] = set()
    refs: list[tuple[str, int, str]] = []
    for fname, lines in files.items():
        for i, line in enumerate(lines):
            def_spans = [
                (m.start(0), m.end(0), m.group(1)) for m in DEF_RE.finditer(line)
            ]
            for _, _, name in def_spans:
                defs.add(name)
            for m in STR_RE.finditer(line):
                # Skip if this quoted string is inside an identifier="..." span
                if any(ds <= m.start(0) and m.end(0) <= de for ds, de, _ in def_spans):
                    continue
                refs.append((fname, i, m.group(1)))

    undefined = [(f, i, name) for f, i, name in refs if name not in defs]
    if undefined:
        f, i, name = undefined[0]
        raise SkipSequence(
            f"validation: {len(undefined)} undefined ref(s); first: "
            f"{name!r} in {f}:{i + 1}"
        )


class SkipSequence(Exception):
    """Raised when the tool declines to extract a sequence (no files written)."""


def verify_occurrence(
    fname: str, idx: int, expected_classes: list[str], lines: list[str]
) -> None:
    """Verify line class names at target indices match the expected sequence."""
    N = len(expected_classes)
    for p in range(N):
        line_idx = LINE_BASE + idx + p
        if line_idx >= len(lines):
            raise SkipSequence(f"{fname}@{idx + p}: past end of file")
        actual = line_class(lines[line_idx])
        expected = expected_classes[p]
        if actual != expected:
            raise SkipSequence(
                f"stale/already-extracted: {fname}@{idx + p} "
                f"expected {expected}, got {actual!r}"
            )


def extract(seq_num: int) -> None:
    seqs = parse_report(REPORT_PATH)
    if seq_num not in seqs:
        sys.exit(f"sequence {seq_num} not in report")
    seq = seqs[seq_num]
    if seq["bank"] != BANK_LABEL:
        sys.exit(f"sequence {seq_num} is bank {seq['bank']}, not {BANK_LABEL}")

    N = seq["length"]
    locs = seq["locations"]
    expected_classes = seq["expected_classes"]
    if len(locs) < 2:
        sys.exit(f"sequence {seq_num} has <2 occurrences; nothing to extract")
    if len(expected_classes) != N:
        sys.exit(
            f"sequence {seq_num}: Commands list ({len(expected_classes)}) "
            f"doesn't match Length ({N})"
        )

    # Load all bank 35 files into memory
    files: dict[str, list[str]] = {}
    for p in sorted(BANK_PATH.glob("*.py")):
        if p.name == "__init__.py":
            continue
        files[p.name] = p.read_text().splitlines(keepends=True)

    # Safety: verify every occurrence matches expected class names BEFORE editing
    for fname, idx in locs:
        if fname not in files:
            sys.exit(f"{fname}: unknown file in bank {BANK_LABEL}")
        verify_occurrence(fname, idx, expected_classes, files[fname])

    # Source = first occurrence
    source_file, source_idx = locs[0]
    source_lines = files[source_file]

    source_idents: list[str | None] = []
    for p in range(N):
        m = IDENT_RE.search(source_lines[LINE_BASE + source_idx + p])
        source_idents.append(m.group(1) if m else None)

    if source_idents[0] is None:
        source_idents[0] = f"extracted_subr_{uuid.uuid4().hex}"

    # Walk other occurrences, collect renames
    renames: dict[str, str] = {}
    for fname, idx in locs[1:]:
        lines = files[fname]
        for p in range(N):
            m = IDENT_RE.search(lines[LINE_BASE + idx + p])
            if not m:
                continue
            occ_ident = m.group(1)
            if source_idents[p] is None:
                source_idents[p] = f"extracted_subr_pos{p}_{uuid.uuid4().hex}"
            src_ident = source_idents[p]
            assert src_ident is not None
            if occ_ident != src_ident:
                if occ_ident in renames and renames[occ_ident] != src_ident:
                    raise SkipSequence(
                        f"conflict: identifier {occ_ident} would be renamed to both "
                        f"{renames[occ_ident]} and {src_ident}"
                    )
                renames[occ_ident] = src_ident

    # Apply source identifier updates (in place, no line-count change)
    for p in range(N):
        src_ident = source_idents[p]
        if src_ident is None:
            continue
        ln = LINE_BASE + source_idx + p
        m_cur = IDENT_RE.search(source_lines[ln])
        if m_cur and m_cur.group(1) == src_ident:
            continue
        source_lines[ln] = set_identifier(source_lines[ln], src_ident)

    # Apply global renames (only within quoted string literals)
    if renames:
        for fname, lines in files.items():
            for i, line in enumerate(lines):
                modified = line
                for old, new in renames.items():
                    modified = modified.replace(f'"{old}"', f'"{new}"')
                if modified != line:
                    lines[i] = modified

    # Replace each non-source occurrence with a single Jmp line, descending idx per file
    jmp_ident = source_idents[0]
    indent_match = re.match(r"^(\s*)", source_lines[LINE_BASE + source_idx])
    indent = indent_match.group(1) if indent_match else "\t"
    jmp_line = f'{indent}Jmp(["{jmp_ident}"]),\n'

    file_to_occs: dict[str, list[int]] = {}
    for fname, idx in locs[1:]:
        file_to_occs.setdefault(fname, []).append(idx)

    for fname, indices in file_to_occs.items():
        lines = files[fname]
        for idx in sorted(indices, reverse=True):
            start = LINE_BASE + idx
            end = start + N
            lines[start:end] = [jmp_line]

    # Pre-write validation: every quoted string referenced as a destination must
    # resolve to a definition somewhere in the bank. Treats `identifier="X"` as
    # the only definition form; every other quoted string is a reference.
    validate_identifier_graph(files)

    # Write modified files back
    written = 0
    for fname, lines in files.items():
        p = BANK_PATH / fname
        new_text = "".join(lines)
        if p.read_text() != new_text:
            p.write_text(new_text)
            written += 1

    print(f"sequence #{seq_num}: source={source_file}@{source_idx} jmp_ident={jmp_ident}")
    print(f"  {len(locs) - 1} occurrence(s) replaced, {len(renames)} identifier(s) renamed")
    print(f"  {written} file(s) written")
    if renames:
        for old, new in sorted(renames.items()):
            print(f"    rename {old} -> {new}")


def run_analyzer() -> None:
    result = subprocess.run(
        [str(PYTHON), str(ANALYZER)], cwd=REPO_ROOT, capture_output=True, text=True
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        sys.exit("analyzer failed")


def run_assembler() -> None:
    result = subprocess.run(
        [str(PYTHON), str(MANAGE_PY), "animationassembler", "--rom", "/mnt/d/smrpg.sfc"],
        cwd=REPO_ROOT,
        env={"PYTHONPATH": "src", "PATH": "/usr/bin:/bin"},
        capture_output=True,
        text=True,
    )
    if "successfully assembled" not in result.stdout:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        sys.exit("assembler failed")


def pick_top_for_bank(
    seqs: dict[int, dict], skipped: set[tuple[str, ...]]
) -> int | None:
    """Pick the highest-savings bank sequence whose class-list isn't skipped."""
    candidates = sorted(
        (
            (num, s)
            for num, s in seqs.items()
            if s["bank"] == BANK_LABEL and len(s["locations"]) >= 2 and s["savings"] > 0
        ),
        key=lambda ns: ns[1]["savings"],
        reverse=True,
    )
    for num, s in candidates:
        if tuple(s["expected_classes"]) in skipped:
            continue
        return num
    return None


def loop_mode(max_count: int) -> None:
    # Content-based skip list (stable across report refreshes).
    skipped: set[tuple[str, ...]] = set()
    need_refresh = True
    seqs: dict[int, dict] = {}
    for i in range(max_count):
        print(f"\n=== iteration {i + 1}/{max_count} ===")
        if need_refresh:
            run_analyzer()
            seqs = parse_report(REPORT_PATH)
            need_refresh = False
        num = pick_top_for_bank(seqs, skipped)
        if num is None:
            print(f"no more eligible bank {BANK_LABEL} sequences")
            return
        s = seqs[num]
        print(f"picking sequence #{num} (savings ~{s['savings']} bytes)")
        try:
            extract(num)
        except SkipSequence as e:
            print(f"  skipped: {e}")
            skipped.add(tuple(s["expected_classes"]))
            continue
        run_assembler()
        print("  assembler OK")
        need_refresh = True


def main() -> None:
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("seq_num", type=int, nargs="?")
    group.add_argument("--loop", action="store_true")
    ap.add_argument("--max", type=int, default=5, help="max iterations for --loop")
    ap.add_argument(
        "--bank",
        default="35",
        help="bank dir under battle_animation/ (e.g. 35, 3A, 02); default 35",
    )
    args = ap.parse_args()

    configure_bank(args.bank)

    if args.loop:
        loop_mode(args.max)
    else:
        extract(args.seq_num)


if __name__ == "__main__":
    main()
