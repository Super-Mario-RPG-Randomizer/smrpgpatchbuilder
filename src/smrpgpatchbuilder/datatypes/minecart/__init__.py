"""Moleville Mountain Mode7 minecart track patch-building primitives.

The randomizer generates a track procedurally and feeds it through these types
to produce a ROM patch. See :mod:`.classes` for the entry points.
"""

from .constants import (
    MAP_H, MAP_W, M7_OBJECTS_PER_MAP, TrackColor, TrackType, background_tile,
    tile_index,
)
from .classes import (
    EAST, NORTH, SOUTH, WEST, MinecartTrack, build_minecart_patch, track_type_for,
)
from .lz3 import compress, decompress

__all__ = [
    "MinecartTrack",
    "build_minecart_patch",
    "track_type_for",
    "TrackType",
    "TrackColor",
    "tile_index",
    "background_tile",
    "compress",
    "decompress",
    "NORTH", "SOUTH", "EAST", "WEST",
    "MAP_W", "MAP_H", "M7_OBJECTS_PER_MAP",
]
