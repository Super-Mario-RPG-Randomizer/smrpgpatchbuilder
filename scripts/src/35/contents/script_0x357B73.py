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

script = AnimationScriptBlock(expected_size=209, expected_beginning=0x357B73, script=[
	ResetTargetMappingMemory(identifier="command_0x357B73"),
	SetAMEM60ToCurrentTarget(identifier="extracted_subr_9da894f876a84ebfb507577078a2e9ff"),
	UnknownCommand(bytearray([0x44, 0x38])),
	Jmp(["extracted_subr_fd991d72e26d46e18a7200d7f7d9088e"]),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=-16, y=8, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x357B83"),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=512, arch_height=0),
	Jmp(["extracted_subr_4b9e085ffed5427caacbe3036f947505"], identifier="extracted_subr_8bf3d117536849fbae321f1b09a0d477"),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x38])),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=128, identifier="extracted_subr_212487dd097146c7bd0ea170c8f41d7a"),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	PlaySound(sound=S0111_SLEDGE),
	ResetObjectMappingMemory(),
	SetAMEM16BitToConst(0x60, 10),
	ResetSpriteSequence(),
	Jmp(["extracted_subr_40d64af0374a47fbb5d640c06a3263c9"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, looping_on=True, identifier="command_0x357BB8"),
	Jmp(["command_0x353E27"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=2048, arch_height=0),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	SpriteSequence(sequence=3),
	ResetObjectMappingMemory(),
	Jmp(["extracted_subr_447f790dbdf740b2914c297ee0ba0ef7"]),
	MoveObject(speed=65, start_position=-513, end_position=256, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	Jmp(["extracted_subr_43b1a2bc065f4e89850d9a1a4b08d157"]),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=128, y=160, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x357BEF"),
	Jmp(["extracted_subr_212487dd097146c7bd0ea170c8f41d7a"]),
	PlaySound(sound=S0149_ENEMY_JUMPS_HIGH),
	MoveObject(speed=17, start_position=-1281, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	Jmp(["extracted_subr_ce8253dd7d1f49919640db74611f9adf"]),
	ReturnSubroutine(),
	SpriteSequence(sequence=4, identifier="command_0x357C11"),
	Jmp(["extracted_subr_f8e41eba8c2b4f67a36f3fbfa40ed6ae"]),
	PlaySound(sound=S0110_HUGE_EXPLOSION, identifier="extracted_subr_3cbdacbccddb4b53b3c1e0828c6c73c8"),
	Jmp(["extracted_subr_839d52ebe6ab45fbb191f16775fef991"]),
	SetAMEM16BitToConst(0x60, 1),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=4, destinations=["command_0x35624B"]),
	StopShakingObject(),
	RunSubroutine(["command_0x352552"]),
	Jmp(["extracted_subr_3cbdacbccddb4b53b3c1e0828c6c73c8"]),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
