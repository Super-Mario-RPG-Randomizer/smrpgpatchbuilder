from smrpgpatchbuilder.datatypes.items.classes import Accessory, Item
from smrpgpatchbuilder.datatypes.items.constants import ITEMS_BASE_ADDRESS
from smrpgpatchbuilder.datatypes.items.enums import EffectType
from smrpgpatchbuilder.datatypes.spells.enums import Status, TempStatBuff

BOTH = EffectType.PROTECTION | EffectType.INFLICTION


class _Charm(Accessory):
    _item_id = 94
    _price = 100


class _Consumable(Item):
    _item_id = 100
    _price = 100
    _effect_type = EffectType.NULLIFICATION


def _effect_byte(item: Item) -> int:
    """Item stat byte 1 as actually written to the ROM."""
    return item.render()[ITEMS_BASE_ADDRESS + item.item_id * 18][1]


def test_equipment_always_enables_both_effect_bits():
    # $C2:BAE8 tests PROTECTION and INFLICTION independently, so an equip can do
    # both. Before this, whichever bit was unset made that half of the data
    # silently inert in-game.
    assert _effect_byte(_Charm()) == BOTH == 0x03

    protect_only = _Charm()
    protect_only.set_status_immunities([Status.MUTE])
    assert _effect_byte(protect_only) == BOTH

    buff_only = _Charm()
    buff_only.set_temp_buffs([TempStatBuff.ATTACK])
    assert _effect_byte(buff_only) == BOTH

    both = _Charm()
    both.set_status_immunities([Status.MUTE])
    both.set_temp_buffs([TempStatBuff.ATTACK])
    assert _effect_byte(both) == BOTH


def test_consumables_keep_their_declared_effect_type():
    # Byte 7 means "inflict these" on a consumable, not "immune to these", so
    # consumables must not be forced to PROTECTION | INFLICTION.
    assert _effect_byte(_Consumable()) == EffectType.NULLIFICATION
