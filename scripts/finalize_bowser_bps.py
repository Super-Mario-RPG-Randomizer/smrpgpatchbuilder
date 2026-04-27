"""Pipeline:
  1. import the bowser-overlay sprite collection from disk
     (after running install_bowser_sprites.py)
  2. render via the existing SpriteCollection
  3. apply rendered bytes plus the bowser map_sprite to the ROM in memory
  4. emit a BPS, with a larger blocksize so the diff finishes in
     reasonable time despite the large zeroed regions
"""
import argparse
import os
import sys
import time
from copy import deepcopy
from datetime import datetime

from bps.io import write_bps

from disassembler_output.sprites.sprites import sprites as sprite_collection
from disassembler_output.sprites.insertions.bowser.map import map_sprite, map_address
from manual_bps import diff_simple

t0 = time.monotonic()
def log(msg: str) -> None:
    print(f"[{time.monotonic()-t0:7.1f}s] {msg}", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rom", required=True)
    parser.add_argument("-o", "--output", default=None)
    args = parser.parse_args()

    log("Reading ROM")
    original = bytearray(open(args.rom, "rb").read())
    rom = deepcopy(original)

    log("Rendering sprite collection")
    output = sprite_collection.render(False)

    log("Applying rendered bytes to ROM")
    for start, bytes_ in output:
        end = start + len(bytes_)
        if end > len(rom):
            raise ValueError(f"write at {start:#X} exceeds ROM size")
        rom[start:end] = bytes_

    log(f"Writing map_sprite ({len(map_sprite)} bytes) at 0x{map_address:06X}")
    rom[map_address:map_address + len(map_sprite)] = map_sprite

    out_path = args.output
    if out_path is None:
        os.makedirs("./src/assembler_output/graphics/bps", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        out_path = f"./src/assembler_output/graphics/bps/smrpg-bowser-{ts}.bps"

    log("Diffing (manual SourceRead/TargetRead encoder)")
    iterable = diff_simple(bytes(original), bytes(rom))
    with open(out_path, "wb") as f:
        write_bps(iterable, f)
    log(f"Wrote BPS: {out_path} ({os.path.getsize(out_path)} bytes)")


if __name__ == "__main__":
    main()
