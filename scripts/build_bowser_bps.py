"""Build a BPS patch that overlays the bowser sprite insertions
(from smrpg_web_randomizer/v9 randomizer/data/sprites/insertions/bowser)
onto the patchbuilder's existing sprite collection, plus the map sprite
write at 0x3E90AA.

Usage:
    PYTHONPATH=src patchvenv/bin/python scripts/build_bowser_bps.py --rom /path/to/smrpg.sfc
"""
import argparse
import os
import sys
from copy import deepcopy
from datetime import datetime

from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress

from smrpgpatchbuilder.datatypes.graphics.classes import (
    AnimationPack,
    AnimationPackProperties,
    AnimationSequence,
    CompleteSprite,
)

from disassembler_output.sprites.sprites import sprites as sprite_collection
from disassembler_output.sprites.insertions.bowser.sprites import sprites as bowser_overrides
from disassembler_output.sprites.insertions.bowser.map import map_sprite, map_address


def make_stub_sprite() -> CompleteSprite:
    return CompleteSprite(
        animation=AnimationPack(
            0,
            length=0,
            unknown=0x0002,
            properties=AnimationPackProperties(
                vram_size=2048, molds=[], sequences=[AnimationSequence(frames=[])]
            ),
        ),
        palette_id=0,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rom", required=True, help="path to base SMRPG ROM")
    parser.add_argument("-w", "--whitespace", action="store_true",
                        help="add whitespace around specific sprites")
    parser.add_argument("-o", "--output", default=None,
                        help="output BPS path (default: src/assembler_output/graphics/bps/smrpg-bowser-<ts>.bps)")
    args = parser.parse_args()

    overridden = [i for i, s in enumerate(bowser_overrides) if s is not None]
    print(f"Overriding sprite indices: {overridden}")
    bowser_set = set(overridden)
    stub = make_stub_sprite()
    for i in range(len(sprite_collection.sprites)):
        if i in bowser_set:
            sprite_collection.sprites[i] = bowser_overrides[i]
        else:
            sprite_collection.sprites[i] = stub
    print(f"Stubbed out {len(sprite_collection.sprites) - len(bowser_set)} non-bowser sprites")

    original_rom = bytearray(open(args.rom, "rb").read())
    rom = deepcopy(original_rom)

    output = sprite_collection.render(args.whitespace)
    for start, bytes_ in output:
        end = start + len(bytes_)
        if end > len(rom):
            raise ValueError(f"sprite write at {start:#X} exceeds ROM size (end {end:#X})")
        rom[start:end] = bytes_

    map_end = map_address + len(map_sprite)
    if map_end > len(rom):
        raise ValueError(f"map sprite write at {map_address:#X} exceeds ROM size")
    rom[map_address:map_end] = map_sprite
    print(f"Wrote map_sprite ({len(map_sprite)} bytes) at 0x{map_address:06X}")

    out_path = args.output
    if out_path is None:
        os.makedirs("./src/assembler_output/graphics/bps", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        out_path = f"./src/assembler_output/graphics/bps/smrpg-bowser-{ts}.bps"

    blocksize = (len(original_rom) + len(rom)) // 1000000 + 1
    iterable = diff_bytearrays(blocksize, bytes(original_rom), bytes(rom))
    with open(out_path, "wb") as f:
        write_bps(bps_progress(iterable), f)
    print(f"Wrote BPS: {out_path}")


if __name__ == "__main__":
    main()
