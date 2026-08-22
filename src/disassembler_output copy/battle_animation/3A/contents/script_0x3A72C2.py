# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from ....variables.sprite_names import *
from ....variables.music_names import *
from ....variables.battle_sfx_names import *
from ....variables.battle_effect_names import *
from ....variables.battle_event_names import *
from ....variables.screen_effect_names import *
from ....spells.spells import *
from ....items.items import *
from ....enemies.enemies import *
from ....enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.battle_targets import *

script = AnimationScriptBlock(expected_size=102, expected_beginning=0x3A72C2, script=[
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1792, arch_height=0, identifier="command_0x3A72C2"),
	Jmp(["command_0x3A7157"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=2048, arch_height=0, identifier="command_0x3A72CB"),
	Jmp(["command_0x3A7157"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=64, arch_height=0, identifier="command_0x3A72D4"),
	Jmp(["command_0x3A7157"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=48, identifier="command_0x3A72DD"),
	Jmp(["command_0x3A71E9"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=96, identifier="command_0x3A72E6"),
	Jmp(["command_0x3A71E9"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=144, identifier="command_0x3A72EF"),
	Jmp(["command_0x3A71E9"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=192, identifier="command_0x3A72F8"),
	Jmp(["command_0x3A71E9"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=240, identifier="command_0x3A7301"),
	Jmp(["command_0x3A71E9"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=288, identifier="command_0x3A730A"),
	Jmp(["command_0x3A71E9"])
])
