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
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x38])),
	Jmp(["command_0x357586"]),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=-16, y=8, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x357B7A"),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=512, arch_height=0),
	Jmp(["command_0x352163"]),
	ResetTargetMappingMemory(identifier="command_0x357B8B"),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x38])),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=128),
	RunSubroutine(["command_0x357EE2"]),
	PlaySound(sound=S0111_SLEDGE),
	ResetObjectMappingMemory(),
	SetAMEM16BitToConst(0x60, 10),
	ResetSpriteSequence(),
	ClearAMEM8Bit(0x6F),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=2, destinations=["command_0x3536D8"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60, identifier="command_0x357BA6"),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, looping_on=True, identifier="command_0x357BAB"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=16, y=-8, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=2048, arch_height=0),
	RunSubroutine(["command_0x357EE2"]),
	SpriteSequence(sequence=3),
	ResetObjectMappingMemory(),
	MoveObject(speed=1, start_position=512, end_position=0, apply_to_x=True, should_set_speed=True),
	RunSubroutine(["command_0x352C1B"]),
	MoveObject(speed=65, start_position=-513, end_position=256, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	Jmp(["command_0x357567"]),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=128, y=160, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x357BD9"),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=128),
	RunSubroutine(["command_0x357EE2"]),
	PlaySound(sound=S0149_ENEMY_JUMPS_HIGH),
	MoveObject(speed=17, start_position=-1281, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20, identifier="command_0x357BF4"),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	SpriteSequence(sequence=4, identifier="command_0x357BFA"),
	ShakeScreen(amount=5, speed=8),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
	PlaySound(sound=S0110_HUGE_EXPLOSION),
	ClearAMEM8Bit(0x68),
	ClearAMEM8Bit(0x60),
	SetAMEM16BitToConst(0x60, 1),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=4, destinations=["command_0x356240"]),
	StopShakingObject(),
	RunSubroutine(["command_0x352538"]),
	PlaySound(sound=S0110_HUGE_EXPLOSION),
	ClearAMEM8Bit(0x68),
	ClearAMEM8Bit(0x60),
	SetAMEM16BitToConst(0x60, 1),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=4, destinations=["command_0x356240"]),
	StopShakingObject(),
	RunSubroutine(["command_0x352538"]),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
