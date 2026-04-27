"""Apply a BPS to a source ROM and confirm CRC trailers + the bowser
write at 0x3E90AA match.
"""
import sys
from zlib import crc32

from bps.apply import apply_to_bytearrays
from bps.io import read_bps

bps_path, rom_path = sys.argv[1], sys.argv[2]
source = bytearray(open(rom_path, "rb").read())
target = bytearray(len(source))

with open(bps_path, "rb") as f:
    instructions = list(read_bps(f))

apply_to_bytearrays(iter(instructions), bytes(source), target)
print(f"Applied. source crc32 = {crc32(bytes(source)):08x}, target crc32 = {crc32(bytes(target)):08x}")

# Spot check: the map_sprite write at 0x3E90AA, first 16 bytes
print("target[0x3E90AA:0x3E90BA] =", target[0x3E90AA:0x3E90BA].hex())
# Sprite data table at 0x250000 — first sprite (bowser sprite_0)
print("target[0x250000:0x250010] =", target[0x250000:0x250010].hex())
