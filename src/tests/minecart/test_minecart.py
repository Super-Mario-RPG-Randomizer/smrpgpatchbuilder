"""Tests for the Moleville Mountain minecart track primitives.

ROM-free: the encoder is checked against its own decoder (the decoder was
validated against the game's actual decompression routine when the format was
reverse-engineered, so a self round-trip is sufficient here)."""

import random

from smrpgpatchbuilder.datatypes.minecart import (
    EAST, MAP_H, MAP_W, NORTH, SOUTH, WEST, MinecartTrack, TrackColor,
    TrackType, background_tile, build_minecart_patch, compress, decompress,
    tile_index, track_type_for,
)
from smrpgpatchbuilder.datatypes.minecart.constants import (
    BLOCK_BASE, HEADER_LEN, NUM_SECTIONS, SECTION_A, SECTION_B, START_X_ADDR,
    START_Y_ADDR, WINDOW_SIZE,
)


def test_codec_round_trips():
    rng = random.Random(0)
    cases = [
        bytes(4096),                                            # all zero
        bytes(rng.randrange(256) for _ in range(4096)),         # incompressible
        bytes((i & 0xFF) for i in range(4096)),                 # ascending
        bytes(background_tile(r, c) for r in range(MAP_H) for c in range(MAP_W)),
        bytes([0x00] * 50 + [0x01] * 50) * 40,                  # flat runs
    ]
    for data in cases:
        assert decompress(compress(data)) == data
    # background texture compresses hard (repeating + ascending)
    bg = bytes(background_tile(r, c) for r in range(MAP_H) for c in range(MAP_W))
    assert len(compress(bg)) < len(bg) // 2


def test_tile_index_and_colors():
    assert tile_index(TrackType.STRAIGHT_NS, TrackColor.GREEN) == 0x00
    assert tile_index(TrackType.STRAIGHT_EW, TrackColor.GREEN) == 0x01
    assert tile_index(TrackType.CORNER_SE, TrackColor.RED) == 0x14
    assert tile_index(TrackType.STRAIGHT_NS, TrackColor.BLUE) == 0x20
    # the colour bands sit below the 0x40 background floor
    assert all(background_tile(r, c) >= 0x40 for r in range(MAP_H) for c in range(MAP_W))


def test_track_type_for_corners():
    assert track_type_for(NORTH, NORTH) == TrackType.STRAIGHT_NS
    assert track_type_for(EAST, EAST) == TrackType.STRAIGHT_EW
    assert track_type_for(NORTH, EAST) == track_type_for(WEST, SOUTH) == TrackType.CORNER_SE
    assert track_type_for(EAST, NORTH) == track_type_for(SOUTH, WEST) == TrackType.CORNER_NW


def _decode_section(block, idx):
    ptr = block[idx * 2] | (block[idx * 2 + 1] << 8)
    return decompress(block, ptr + 1)            # +1 skips the 0x01 section prefix


def test_build_patch_layout_and_roundtrip():
    a, b = MinecartTrack(), MinecartTrack()
    for row in range(MAP_H):
        a.set_track(0, row, TrackType.STRAIGHT_NS)
        b.set_track(row, MAP_H // 2, TrackType.STRAIGHT_EW)
    a.set_track(0, 0, TrackType.STRAIGHT_NS, TrackColor.BLUE)

    patch = build_minecart_patch(a, b, 0, MAP_H - 1)

    assert set(patch) == {BLOCK_BASE, START_X_ADDR, START_Y_ADDR}
    block = patch[BLOCK_BASE]
    assert len(block) <= WINDOW_SIZE
    # start pixel = tile * 16 + 8 -> (8, 1016) for the bottom-left start tile
    assert patch[START_X_ADDR] == bytes([8, 0])
    assert patch[START_Y_ADDR] == bytes([0xF8, 0x03])
    # section pointers are monotonic and start right after the header
    ptrs = [block[i * 2] | (block[i * 2 + 1] << 8) for i in range(NUM_SECTIONS)]
    assert ptrs[0] == HEADER_LEN
    assert ptrs == sorted(ptrs)
    # the freshly compressed maps decode back exactly
    assert _decode_section(block, SECTION_A) == a.tilemap_bytes
    assert _decode_section(block, SECTION_B) == b.tilemap_bytes


def test_objects_and_breaks_scaffold():
    a, b = MinecartTrack(), MinecartTrack()
    a.place_break(10, 10, vertical=True, mushroom=True)      # break + centre object
    b.add_object(5, 5)
    # adding objects rewrites the object section; patch still assembles in budget
    patch = build_minecart_patch(a, b, 0, MAP_H - 1)
    assert len(patch[BLOCK_BASE]) <= WINDOW_SIZE
    assert a.objects == [(10, 10)] and b.objects == [(5, 5)]
