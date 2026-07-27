"""Combine this project's session changes (battle-animation boss edits +
monster AI + formations) into ONE patched ROM and ONE bps, based on a given
SMRPG ROM (the Postgame Additions ROM).

IMPORTANT: the disassembly's battle_animation is a CONDENSED-VANILLA base, so we
overlay ONLY the two blocks we actually edited (0x3A6000 events, 0x3ACF48
outsourced routines) — overlaying the whole bank would clobber the postgame's
own (weapon/attack) animations with vanilla. monster_ai and packs were
disassembled from the postgame ROM, so overlaying their full assembled output
changes only our edits (assuming clean round-trip; we measure that below).

Usage:  PYTHONPATH=src patchvenv/bin/python build_postgame_patch.py <rom> <out_dir>
"""
import sys
import os
import importlib
from copy import deepcopy

from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress

ROM_PATH = sys.argv[1]
OUT_DIR = sys.argv[2]

# battle-animation ROM blocks we edited this/last session (everything else in
# the bank is condensed-vanilla and must NOT overwrite the postgame ROM)
ANIM_BLOCKS = {0x3A6000, 0x3ACF48}

original = bytearray(open(ROM_PATH, "rb").read())


def delta(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def collect_writes():
    """Return list of (start, bytes, source-label)."""
    writes = []
    # 1) battle animation — ONLY the two edited blocks
    # battle animation: overlay ALL of bank 3A. The condensed disassembly is a
    # self-consistent layout; overlaying only 3A6000/3ACF48 left dangling refs
    # into other (non-overlaid) bank-3A files — e.g. event59 -> command_0x3AD902
    # -> Jmp 0x3AB3D2, which landed on the postgame's untouched bytes ("BF data
    # too short"). Overlaying the whole bank makes every 3A cross-ref resolve.
    # Banks 35 (weapon/attack anims) and 02 are LEFT as the postgame's so the
    # custom weapon animations the user confirmed working are preserved.
    bank = importlib.import_module("disassembler_output.battle_animation.3A.export").bank
    for start, b in bank.render():
        writes.append((start, bytes(b), "anim_3A"))
    # 2) monster AI (postgame-disassembled; full overlay)
    ms = importlib.import_module("disassembler_output.monster_ai.monster_scripts").monster_scripts
    out = ms.render()
    writes.append((0x3930AA, bytes(out[0]), "monster_ai 0x3930AA"))
    writes.append((0x39F400, bytes(out[1]), "monster_ai 0x39F400"))
    # 3) formations / packs (postgame-disassembled; full overlay)
    pc = importlib.import_module("disassembler_output.packs.pack_collection").pack_collection
    for start, b in pc.render().items():
        writes.append((start, bytes(b), "packs"))
    # 4) belome3_brooch ASM hook — Belome-3 non-elemental-magic immunity
    #    (monsters 201/125, both verified) + Enduring Brooch survive-at-1HP.
    #    NOTE: brooch is keyed to item id 0x49 (73); in this ROM item 73 is the
    #    vanilla "Spare" placeholder (no Enduring Brooch exists), so the brooch
    #    half is DORMANT unless item 73 is repurposed. Immunity half works.
    #    Free-ROM payload (0x0FF7B0) verified empty; hook sites verified vanilla.
    sys.path.insert(0, "/home/pidge/code/smrpg_web_randomizer")
    from randomizer.patches.asm import belome3_brooch
    for start, b in belome3_brooch.get_patch(False).items():
        writes.append((start, bytes(b), "belome3_brooch"))
    # 5) item 73 -> Enduring Brooch (single-item render = stats record + price +
    #    name; type now Accessory + _prevent_ko). NOTE: only item 73 is overlaid,
    #    not the full ALL_ITEMS table (that render is blocked by pre-existing
    #    postgame item-data bugs: weapon-id>40 etc.). The flavor DESCRIPTION text
    #    is therefore NOT applied (it lives in the packed desc table that needs the
    #    full render); the brooch is functional + correctly named without it.
    brooch = importlib.import_module("disassembler_output.items.items").SpareItem2()
    for start, b in brooch.render().items():
        writes.append((start, bytes(b), "item73_brooch"))
    return writes


writes = collect_writes()

# per-source contribution (overlay each onto a fresh copy of the source ROM)
print("=== per-source byte deltas vs source ROM ===")
by_source = {}
for start, b, label in writes:
    src = label.split()[0] if label.startswith(("anim", "monster_ai")) else label
    tmp = original[start:start + len(b)]
    by_source.setdefault(src, 0)
    by_source[src] += delta(tmp, b)
for src, n in sorted(by_source.items()):
    print(f"  {src:24s} {n:7d} bytes differ")

# build combined patched ROM
rom = deepcopy(original)
for start, b, label in writes:
    end = start + len(b)
    if end > len(rom):
        raise ValueError(f"{label}: {start:#X}..{end:#X} exceeds ROM")
    rom[start:end] = b

total = delta(original, rom)
print(f"=== total: {total} bytes differ from source ROM ({len(writes)} regions) ===")

os.makedirs(OUT_DIR, exist_ok=True)

# per-region .bin files for the "nuclear replacement" regions (battle events =
# bank 3A, and monster AI). Each is named by its ROM file offset, so you can
# clobber that offset in a hex editor. (packs/items/brooch are small/scattered
# and already in the patched ROM below.)
bindir = os.path.join(OUT_DIR, "bin")
os.makedirs(bindir, exist_ok=True)
nbins = 0
for start, b, label in writes:
    if label == "anim_3A" or label.startswith("monster_ai"):
        with open(os.path.join(bindir, f"write_to_0x{start:06X}.bin"), "wb") as f:
            f.write(b)
        nbins += 1
print(f"wrote {nbins} region .bin files (bank 3A + monster AI) to {bindir}/")

patched_path = os.path.join(OUT_DIR, "Postgame Additions + boss fights.smc")
with open(patched_path, "wb") as f:
    f.write(rom)
blocksize = (len(original) + len(rom)) // 1000000 + 1
bps_path = os.path.join(OUT_DIR, "postgame_boss_fights.bps")
with open(bps_path, "wb") as f:
    write_bps(bps_progress(diff_bytearrays(blocksize, bytes(original), bytes(rom))), f)
print(f"patched ROM: {patched_path}")
print(f"bps patch:   {bps_path}")
