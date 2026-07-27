"""Materialize a sprite overlay to disk so the existing
graphicsassembler / finalize_*_bps pipeline can use it.

For each index in `--keep`, copy
  src/disassembler_output/sprites/insertions/<source>/sprite_<i>.py
into
  src/disassembler_output/sprites/objects/sprite_<i>.py.
For every other index 0..1023, write an empty-mold stub.
"""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OBJECTS = ROOT / "src/disassembler_output/sprites/objects"
INSERTIONS = ROOT / "src/disassembler_output/sprites/insertions"

STUB_TEMPLATE = """# stub (overwritten by install_sprite_overlay.py)
from smrpgpatchbuilder.datatypes.graphics.classes import (
    CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence,
)
sprite = CompleteSprite(
    animation=AnimationPack(0, length=0, unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[],
            sequences=[AnimationSequence(frames=[])],
        ),
    ),
    palette_id=0,
)
"""


def parse_indices(spec: str) -> set[int]:
    out: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            a, b = token.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(token))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True,
                        help="folder under insertions/ containing sprite_*.py")
    parser.add_argument("--keep", required=True,
                        help="indices to copy from source. e.g. '0-30' or '0,1,5-10'")
    args = parser.parse_args()

    keep = parse_indices(args.keep)
    src_dir = INSERTIONS / args.source
    if not src_dir.is_dir():
        raise SystemExit(f"source dir not found: {src_dir}")

    copied = 0
    stubbed = 0
    for i in range(1024):
        target = OBJECTS / f"sprite_{i}.py"
        if i in keep:
            src = src_dir / f"sprite_{i}.py"
            if not src.is_file():
                raise SystemExit(f"missing source sprite_{i}.py in {src_dir}")
            shutil.copyfile(src, target)
            copied += 1
        else:
            target.write_text(STUB_TEMPLATE)
            stubbed += 1
    print(f"Copied {copied} from {src_dir.name}, stubbed {stubbed}")


if __name__ == "__main__":
    main()
