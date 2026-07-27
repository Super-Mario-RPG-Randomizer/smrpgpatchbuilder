"""Build a Moleville Mountain Mode7 minecart track and emit a ROM patch.

The randomizer's procedural generator decides *where* the rails go and *which
way* the cart turns at each cell; this module owns the SMRPG-specific encoding:
tile indices, the background texture, jump-gap squares, LC_LZ3 compression, and
rebuilding the fixed ``$388000`` data window (rewriting Map A/B while copying
every other compressed section byte-for-byte).

Typical use::

    a = MinecartTrack()
    a.set_track(col, row, TrackType.STRAIGHT_NS)          # ... lay the path ...
    a.set_track(end_col, end_row, TrackType.STRAIGHT_NS, TrackColor.BLUE)
    patch = build_minecart_patch(a, b, start_col, start_row)   # dict[int, bytes]
"""

from typing import Dict, List, Optional, Tuple

from .constants import (
    BLOCK_BASE, HEADER_LEN, MAP_H, MAP_W, M7_OBJECTS_PER_MAP, NUM_SECTIONS,
    SECTION_A, SECTION_B, SECTION_OBJECTS, SECTION_PREFIX, START_X_ADDR,
    START_Y_ADDR, TILE_CENTER, TILE_PX, VANILLA_DATA_END, WINDOW_SIZE,
    BREAK_EW, BREAK_NS, TrackColor, TrackType, background_tile, tile_index,
)
from .lz3 import compress
from ._vanilla_block import VANILLA_BLOCK, VANILLA_OBJECTS

# Compass directions used to describe cart motion through a cell.
NORTH, SOUTH, EAST, WEST = "N", "S", "E", "W"

# (in_dir, out_dir) -> non-fork corner type. A corner connects two tile edges;
# both traversal directions of the same physical corner map to one type.
_CORNERS = {
    (NORTH, EAST): TrackType.CORNER_SE, (WEST, SOUTH): TrackType.CORNER_SE,
    (EAST, SOUTH): TrackType.CORNER_SW, (NORTH, WEST): TrackType.CORNER_SW,
    (SOUTH, EAST): TrackType.CORNER_NE, (WEST, NORTH): TrackType.CORNER_NE,
    (EAST, NORTH): TrackType.CORNER_NW, (SOUTH, WEST): TrackType.CORNER_NW,
}


def track_type_for(in_dir: str, out_dir: str) -> TrackType:
    """Straight or corner :class:`TrackType` for a cell entered going ``in_dir``
    and left going ``out_dir`` (compass letters). Forks are placed explicitly."""
    if in_dir == out_dir:
        return TrackType.STRAIGHT_NS if in_dir in (NORTH, SOUTH) else TrackType.STRAIGHT_EW
    try:
        return _CORNERS[(in_dir, out_dir)]
    except KeyError:
        raise ValueError(f"no track tile for turn {in_dir!r}->{out_dir!r} (U-turn?)")


class MinecartTrack:
    """A single 64x64 Mode7 map: background texture plus overlaid rail tiles."""

    def __init__(self) -> None:
        self._grid = bytearray(
            background_tile(r, c) for r in range(MAP_H) for c in range(MAP_W)
        )
        # Mode7 objects (mushrooms/coins): list of (col, row) tile positions.
        self.objects: List[Tuple[int, int]] = []

    def _check(self, col: int, row: int) -> None:
        if not (0 <= col < MAP_W and 0 <= row < MAP_H):
            raise ValueError(f"cell ({col},{row}) out of the {MAP_W}x{MAP_H} map")

    def set_track(self, col: int, row: int, track_type: int,
                  color: int = TrackColor.GREEN) -> None:
        """Place a rail tile of ``track_type``/``color`` at ``(col, row)``."""
        self._check(col, row)
        self._grid[row * MAP_W + col] = tile_index(track_type, color)

    def place_break(self, col: int, row: int, vertical: bool,
                    mushroom: bool = False) -> None:
        """Stamp a jump-gap: the 3x3 break square centred on ``(col, row)``.

        ``vertical`` selects the N/S square (for a N/S track) vs the E/W square.
        ``mushroom`` adds a Mode7 object at the centre (where it must sit).
        """
        self._check(col, row)
        square = BREAK_NS if vertical else BREAK_EW
        for dr in range(3):
            for dc in range(3):
                rr, cc = row + dr - 1, col + dc - 1
                if 0 <= rr < MAP_H and 0 <= cc < MAP_W:
                    self._grid[rr * MAP_W + cc] = square[dr][dc]
        if mushroom:
            self.add_object(col, row)

    def add_object(self, col: int, row: int) -> None:
        """Add a Mode7 object (mushroom/coin) at a tile position."""
        self._check(col, row)
        if len(self.objects) >= M7_OBJECTS_PER_MAP:
            raise ValueError(f"at most {M7_OBJECTS_PER_MAP} Mode7 objects per map")
        self.objects.append((col, row))

    @property
    def tilemap_bytes(self) -> bytes:
        return bytes(self._grid)


def _rebuild_objects(track_a: MinecartTrack, track_b: MinecartTrack) -> Optional[bytes]:
    """Decompressed "object & screen data" with Map A/B Mode7 object positions
    overwritten, or ``None`` if neither map placed any object (copy vanilla)."""
    if not track_a.objects and not track_b.objects:
        return None
    data = bytearray(VANILLA_OBJECTS)
    m7 = data[0] | (data[1] << 8)              # sub-pointer to the 16 object slots
    for slot_base, track in ((m7, track_a), (m7 + 2 * M7_OBJECTS_PER_MAP, track_b)):
        for i, (col, row) in enumerate(track.objects):
            data[slot_base + i * 2] = col & 0xFF
            data[slot_base + i * 2 + 1] = row & 0xFF
    return bytes(data)


def build_minecart_patch(track_a: MinecartTrack, track_b: MinecartTrack,
                         start_col: int, start_row: int) -> Dict[int, bytes]:
    """Assemble the ROM patch for both Mode7 maps.

    Rebuilds the ``$388000`` window with freshly-compressed Map A/B (and rewritten
    Mode7 objects if any), copying all other sections verbatim, and sets the
    shared start pixel to ``(start_col, start_row)``. Returns ``{addr: bytes}``.
    Raises if the rebuilt window would exceed its hard 0x8000 bound.
    """
    ptrs = [VANILLA_BLOCK[2 * i] | (VANILLA_BLOCK[2 * i + 1] << 8)
            for i in range(NUM_SECTIONS)]

    def vanilla_section(idx: int) -> bytes:
        end = ptrs[idx + 1] if idx + 1 < NUM_SECTIONS else VANILLA_DATA_END
        return VANILLA_BLOCK[ptrs[idx]:end]

    new_objects = _rebuild_objects(track_a, track_b)

    out = bytearray(HEADER_LEN)
    new_ptrs = [0] * NUM_SECTIONS
    cursor = HEADER_LEN
    for idx in range(NUM_SECTIONS):
        new_ptrs[idx] = cursor
        if idx == SECTION_A:
            section = bytes([SECTION_PREFIX]) + compress(track_a.tilemap_bytes)
        elif idx == SECTION_B:
            section = bytes([SECTION_PREFIX]) + compress(track_b.tilemap_bytes)
        elif idx == SECTION_OBJECTS and new_objects is not None:
            section = bytes([SECTION_PREFIX]) + compress(new_objects)
        else:
            section = vanilla_section(idx)
        out += section
        cursor += len(section)

    if cursor > WINDOW_SIZE:
        raise ValueError(
            f"rebuilt minecart data is {cursor:#x} bytes, exceeds the "
            f"{WINDOW_SIZE:#x} window by {cursor - WINDOW_SIZE} bytes "
            f"(track too complex to compress in place)"
        )

    for idx in range(NUM_SECTIONS):
        out[idx * 2] = new_ptrs[idx] & 0xFF
        out[idx * 2 + 1] = (new_ptrs[idx] >> 8) & 0xFF

    start_x = start_col * TILE_PX + TILE_CENTER
    start_y = start_row * TILE_PX + TILE_CENTER
    return {
        BLOCK_BASE: bytes(out),
        START_X_ADDR: bytes([start_x & 0xFF, (start_x >> 8) & 0xFF]),
        START_Y_ADDR: bytes([start_y & 0xFF, (start_y >> 8) & 0xFF]),
    }
