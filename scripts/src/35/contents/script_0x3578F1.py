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

script = AnimationScriptBlock(expected_size=44, expected_beginning=0x3578F1, script=[
	Jmp(["command_0x3577E2"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=1536, arch_height=0),
	SetAMEM16BitToConst(0x60, 10, identifier="extracted_subr_5601138440054821ab832dc81177625f"),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	VisibilityOff(unknown_byte=0x01),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	VisibilityOn(unknown_byte=0x01),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	Jmp(["extracted_subr_18e35c801dd342daae7651e5955f4857"]),
	ReturnSubroutine()
])
