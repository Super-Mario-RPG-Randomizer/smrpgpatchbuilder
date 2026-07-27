"""Tests for RoomCollection NPC table construction."""

from smrpgpatchbuilder.datatypes.levels.classes import (
    NPC,
    Room,
    RegularNPC,
    RegularClone,
)
from smrpgpatchbuilder.datatypes.levels.room_collection import RoomCollection


FORCE_FIRST_SPRITE = 799
EMPTY_SPRITE = 1023
ROOM_NPC_SPRITE = 100
CLONE_NPC_SPRITE = 101


def _build_rooms(populated_room: Room | None) -> list[Room | None]:
    """Build a 512-length room list with one optionally-populated room.

    Room 511 must be None per RoomCollection's constructor assertion.
    """
    rooms: list[Room | None] = [None] * 512
    if populated_room is not None:
        rooms[0] = populated_room
    return rooms


def _collection(rooms: list[Room | None]) -> RoomCollection:
    return RoomCollection(
        rooms,
        force_first_npc=NPC(sprite_id=FORCE_FIRST_SPRITE),
        empty_npc=NPC(sprite_id=EMPTY_SPRITE),
    )


def test_force_first_npc_survives_with_no_force_id_npcs():
    """force_first_npc must stay at index 0 even when no room NPC has a force_id.

    Regression: min_table_size stayed 0 when nothing had a force_id, so the
    allocator seeded next_index_after_forced at 0 and overwrote force_first_npc
    with the first standalone NPC.
    """
    room = Room(objects=[RegularNPC(npc=NPC(sprite_id=ROOM_NPC_SPRITE))])
    collection = _collection(_build_rooms(room))

    clone_groups = collection._collect_clone_group_requirements()
    npc_table, _ = collection._build_sequential_placement(clone_groups)

    assert npc_table[0].sprite_id == FORCE_FIRST_SPRITE
    # The standalone room NPC must be placed after index 0, not on top of it.
    assert ROOM_NPC_SPRITE in [npc.sprite_id for npc in npc_table[1:]]


def test_force_first_npc_survives_with_clone_group():
    """A clone group must not be allocated starting at index 0 over force_first_npc.

    Clone groups use get_contiguous_indices, which (without the fix) would also
    start at index 0 because next_index_after_forced was seeded from a
    min_table_size of 0.
    """
    room = Room(
        objects=[
            RegularNPC(npc=NPC(sprite_id=ROOM_NPC_SPRITE)),
            RegularClone(npc=NPC(sprite_id=CLONE_NPC_SPRITE)),
        ]
    )
    collection = _collection(_build_rooms(room))

    clone_groups = collection._collect_clone_group_requirements()
    npc_table, _ = collection._build_sequential_placement(clone_groups)

    assert npc_table[0].sprite_id == FORCE_FIRST_SPRITE
    placed = [npc.sprite_id for npc in npc_table[1:]]
    assert ROOM_NPC_SPRITE in placed
    assert CLONE_NPC_SPRITE in placed


def test_force_first_npc_survives_with_empty_rooms():
    """force_first_npc must still occupy index 0 when no room has any NPC."""
    collection = _collection(_build_rooms(None))

    clone_groups = collection._collect_clone_group_requirements()
    npc_table, _ = collection._build_sequential_placement(clone_groups)

    assert len(npc_table) == 1
    assert npc_table[0].sprite_id == FORCE_FIRST_SPRITE
