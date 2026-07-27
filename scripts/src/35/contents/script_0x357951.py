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

script = AnimationScriptBlock(expected_size=80, expected_beginning=0x357951, script=[
	ReturnSubroutine(identifier="command_0x357951"),
	ResetTargetMappingMemory(identifier="command_0x357952"),
	ResetObjectMappingMemory(),
	MoveObject(speed=257, start_position=1024, end_position=2048, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	Jmp(["extracted_subr_36c21a2106dd4a348b973c381e5b2800"]),
	Jmp(["extracted_subr_60bc895b2cd9494d9d1fde752e7e23e4"]),
	UnknownCommand(bytearray([0x5A])),
	VisibilityOff(unknown_byte=0x01),
	Jmp(["extracted_subr_f298f4de691e4fc592da9ab97a9e7344"]),
	UnknownCommand(bytearray([0x44, 0x60])),
	Jmp(["extracted_subr_3132421ede7a4261a7d8e138cc173fc2"]),
	SetAMEM60ToCurrentTarget(),
	Jmp(["extracted_subr_a53d7f1f83c74948a6caeaa1054bf05c"]),
	VisibilityOn(unknown_byte=0x01),
	PlaySound(sound=S0170_SUBMERGED_UNDER),
	MoveObject(speed=257, start_position=-1025, end_position=-2049, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	UnknownCommand(bytearray([0x59])),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x352552"]),
	ReturnSubroutine()
])
