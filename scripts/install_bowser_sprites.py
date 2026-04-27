"""Materialize the bowser-only sprite layout to disk so the existing
graphicsassembler command can run against it.

Action:
  - For each non-bowser sprite index 0..1023, overwrite
    src/disassembler_output/sprites/objects/sprite_<i>.py with a tiny
    empty-mold stub.
  - For each bowser index, copy
    src/disassembler_output/sprites/insertions/bowser/sprite_<i>.py
    to src/disassembler_output/sprites/objects/sprite_<i>.py.
  - Leaves disassembler_output/sprites/sprites.py unchanged
    (it imports every sprite_<i>; both stubs and bowser overrides match).

After running this, run the existing assembler:
    PYTHONPATH=src patchvenv/bin/python src/smrpgpatchbuilder/manage.py \
        graphicsassembler --rom /path/to/smrpg.sfc

Then write the map sprite separately (see scripts/write_bowser_map.py)
or apply it manually at 0x3E90AA. The graphicsassembler doesn't touch
that address.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OBJECTS = ROOT / "src/disassembler_output/sprites/objects"
BOWSER = ROOT / "src/disassembler_output/sprites/insertions/bowser"

BOWSER_INDICES = [0, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18,
                  96, 132, 135, 136, 621, 634]

STUB_TEMPLATE = """# stub (overwritten by install_bowser_sprites.py)
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


def main() -> None:
    bowser_set = set(BOWSER_INDICES)
    stub_count = 0
    for i in range(1024):
        target = OBJECTS / f"sprite_{i}.py"
        if i in bowser_set:
            src = BOWSER / f"sprite_{i}.py"
            shutil.copyfile(src, target)
        else:
            target.write_text(STUB_TEMPLATE)
            stub_count += 1
    print(f"Wrote {stub_count} stubs and {len(bowser_set)} bowser sprites to {OBJECTS}")


if __name__ == "__main__":
    main()
