"""Constants for the Moleville Mountain Mode7 minecart tracks.

All values verified against vanilla ``smrpg.sfc``. The two Mode7 stages (Map A =
stage 1, Map B = stage 3) are 64x64 metatile grids; the minecart auto-follows
the rail tiles, so the *tile type* at each cell encodes the direction/turn/fork
and the *colour* encodes speed / stage-end. ``tile = colour*0x10 + type``.
"""

from enum import IntEnum

# --- ROM layout (raw file offsets) -----------------------------------------
BLOCK_BASE = 0x388000          # start of the Moleville minigame data window
WINDOW_SIZE = 0x8000           # the window is hard-bounded; 0x390000 = monster data
HEADER_LEN = 0x1E              # 15 little-endian section pointers
NUM_SECTIONS = 15
SECTION_A = 4                  # section index of Map A tilemap (header offset 0x08)
SECTION_B = 5                  # section index of Map B tilemap (header offset 0x0A)
SECTION_OBJECTS = 14           # "object & screen data" (header offset 0x1C)
SECTION_PREFIX = 0x01          # one byte before each compressed stream (loader skips it)
VANILLA_DATA_END = 0x7644      # end of used data in the window (slack to 0x8000 = 2492 B)

START_X_ADDR = 0x039670        # short: minecart start pixel X (operand in init ASM)
START_Y_ADDR = 0x039679        # short: minecart start pixel Y
MUSIC_ADDR = 0x0393EF          # byte: stage music id

# --- tilemap geometry ------------------------------------------------------
MAP_W = 64
MAP_H = 64
TILE_PX = 16                   # each metatile is 16x16 px
TILE_CENTER = TILE_PX // 2     # start pixel = tile * 16 + 8 (centre of the tile)
M7_OBJECTS_PER_MAP = 8         # mushroom/coin slots per map (Mode7 objects)


class TrackColor(IntEnum):
    GREEN = 0   # normal speed (default)
    RED = 1     # must slow down (warning before tight turns)
    BLUE = 2    # stage-end marker (advances to the next stage)
    AQUA = 3    # unused (behaves like blue)


class TrackType(IntEnum):
    """Rail tile semantics (cart motion in -> out). 0-1 straight, 4-7 corners,
    2/3/8-15 forks. See the per-value comments for the exact turn each encodes."""
    STRAIGHT_NS = 0   # driving north/south
    STRAIGHT_EW = 1   # driving east/west
    FORK_N_END_EW = 2  # north path ends, choose east or west
    FORK_S_END_EW = 3  # south path ends, choose east or west
    CORNER_SE = 4     # N->E or W->S  (connects the south & east tile edges)
    CORNER_SW = 5     # E->S or N->W
    CORNER_NE = 6     # S->E or W->N
    CORNER_NW = 7     # E->N or S->W
    FORK_W_CONT_S = 8   # going west: continue west or turn south
    FORK_E_CONT_S = 9   # going east: continue east or turn south
    FORK_W_CONT_N = 10  # going west: continue west or turn north
    FORK_E_CONT_N = 11  # going east: continue east or turn north
    FORK_N_CONT_E = 12  # going north: continue north or turn east
    FORK_N_CONT_W = 13  # going north: continue north or turn west
    FORK_S_CONT_E = 14  # going south: continue south or turn east
    FORK_S_CONT_W = 15  # going south: continue south or turn west


def tile_index(track_type: int, color: int) -> int:
    """Mode7 metatile index for a (type, colour). ``tile = colour*0x10 + type``."""
    return (int(color) << 4) | int(track_type)


def background_tile(row: int, col: int) -> int:
    """The vanilla "empty space" brick texture (metatiles 0x40-0x95)."""
    return 0x40 + 0x10 * (row % 6) + ((col + 3 * ((row // 6) % 2)) % 6)


# --- break (jump gap) 3x3 squares, indexed [drow][dcol]; centre = mushroom slot
BREAK_NS = ((0x46, 0xA0, 0x48), (0xA1, 0xB0, 0xC1), (0x66, 0xC0, 0x68))
BREAK_EW = ((0x46, 0x47, 0x48), (0xA1, 0xB1, 0xC1), (0x66, 0x67, 0x68))
