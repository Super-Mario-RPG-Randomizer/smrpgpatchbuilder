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

script = AnimationScriptBlock(expected_size=50, expected_beginning=0x35791E, script=[
	ResetTargetMappingMemory(identifier="command_0x35791E"),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x48])),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=128),
	Jmp(["extracted_subr_18e35c801dd342daae7651e5955f4857"], identifier="extracted_subr_4b9e085ffed5427caacbe3036f947505"),
	Jmp(["command_0x3577E2"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=256),
	SpriteSequence(sequence=0, mirror=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	SpriteSequence(sequence=1, mirror=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
	SpriteSequence(sequence=1),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
	SpriteSequence(sequence=0),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=1),
	ReturnSubroutine()
])
