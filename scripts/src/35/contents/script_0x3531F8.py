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

script = AnimationScriptBlock(expected_size=217, expected_beginning=0x3531F8, script=[
	SpriteSequence(sequence=4, identifier="command_0x3531F8"),
	Jmp(["extracted_subr_pos1_1a12b5182f13443eb308dfb7c4f4c0cc"]),
	SpriteSequence(sequence=2, identifier="command_0x3531FF"),
	PauseScriptUntilSpriteSequenceDone(),
	Jmp(["command_0x3531FF"]),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	Jmp(["command_0x3505D5"]),
	Jmp(["command_0x3531FF"]),
	Jmp(["extracted_subr_pos1_1a12b5182f13443eb308dfb7c4f4c0cc"]),
	RunSubroutine(["command_0x35322B"], identifier="command_0x353219"),
	Jmp(["command_0x3505D5"]),
	RunSubroutine(["command_0x35322B"], identifier="command_0x35321F"),
	Jmp(["command_0x3508B5"]),
	RunSubroutine(["command_0x35322B"], identifier="command_0x353225"),
	Jmp(["command_0x3509AE"]),
	SpriteSequence(sequence=0, mirror=True, identifier="command_0x35322B"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	SpriteSequence(sequence=1, mirror=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	PlaySound(sound=S0062_MONSTER_RUN_AWAY),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=22, y=-8, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=128),
	Jmp(["extracted_subr_fb9412a09b534997a721442c56c64753"]),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=72, y=-36, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=192),
	Jmp(["extracted_subr_fb9412a09b534997a721442c56c64753"]),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=192, y=-96, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=256),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE, identifier="extracted_subr_0515400c7b5b49018dea377c151cc697"),
	UnknownCommand(bytearray([0xD6])),
	ReturnSubroutine(identifier="extracted_subr_pos2_bf26ea68a9ba447790f714fb34a8fd3f"),
	Jmp(["command_0x35322B"]),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=100, y=-100, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X04, speed=1280, arch_height=208),
	Jmp(["extracted_subr_0515400c7b5b49018dea377c151cc697"]),
	ClearAMEM8Bit(0x6D, identifier="command_0x353297"),
	SetAMEM8BitToConst(0x6D, 1),
	Pause1Frame(identifier="command_0x35329D"),
	SetAMEMToAMEM8Bit(dest_amem=0x68, upper=0x40, amem=0x6A),
	SetAMEMToAMEM8Bit(dest_amem=0x67, upper=0x40, amem=0x6D),
	IncAMEM8BitByAMEM(amem=0x6A, source_amem=0x6C, upper=0x60),
	JmpIfAMEM8BitGreaterOrEqualThanAMEM(amem=0x6A, source_amem=0x6B, upper=0x60, destinations=["extracted_subr_pos2_bf26ea68a9ba447790f714fb34a8fd3f"]),
	Jmp(["command_0x35329D"]),
	Jmp(["extracted_subr_pos2_bf26ea68a9ba447790f714fb34a8fd3f"]),
	DecAMEM8BitByAMEM(amem=0x6A, source_amem=0x6C, upper=0x60),
	JmpIfAMEM8BitLessThanAMEM(amem=0x6A, source_amem=0x6B, upper=0x60, destinations=["command_0x3532D0"]),
	Jmp(["command_0x35329D"]),
	ReturnSubroutine(identifier="command_0x3532D0")
])
