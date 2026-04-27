"""Render the on-disk SpriteCollection (after install_sprite_overlay.py),
optionally overlay an extra `map.py` write, and emit a BPS via the
manual SourceRead/TargetRead encoder.
"""
import argparse
import importlib
import os
import time
from copy import deepcopy
from datetime import datetime

from bps.io import write_bps

from disassembler_output.sprites.sprites import sprites as sprite_collection
from manual_bps import diff_simple

t0 = time.monotonic()
def log(msg: str) -> None:
    print(f"[{time.monotonic()-t0:7.1f}s] {msg}", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rom", required=True)
    parser.add_argument("-o", "--output", default=None)
    parser.add_argument("--map-module", default=None,
                        help="optional dotted module exposing `map_sprite` "
                             "and `map_address`, written verbatim after render")
    parser.add_argument("--label", default="sprite",
                        help="filename prefix for the BPS")
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

    if args.map_module:
        m = importlib.import_module(args.map_module)
        log(f"Writing map_sprite ({len(m.map_sprite)} bytes) at 0x{m.map_address:06X}")
        rom[m.map_address:m.map_address + len(m.map_sprite)] = m.map_sprite

    out_path = args.output
    if out_path is None:
        os.makedirs("./src/assembler_output/graphics/bps", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        out_path = f"./src/assembler_output/graphics/bps/smrpg-{args.label}-{ts}.bps"

    log("Diffing (manual SourceRead/TargetRead encoder)")
    iterable = diff_simple(bytes(original), bytes(rom))
    with open(out_path, "wb") as f:
        write_bps(iterable, f)
    log(f"Wrote BPS: {out_path} ({os.path.getsize(out_path)} bytes)")


if __name__ == "__main__":
    main()
