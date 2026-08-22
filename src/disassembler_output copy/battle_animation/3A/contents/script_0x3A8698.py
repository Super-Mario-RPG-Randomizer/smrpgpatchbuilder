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

script = AnimationScriptBlock(expected_size=292, expected_beginning=0x3A8698, script=[
	PlaySound(sound=S0111_SLEDGE, identifier="command_0x3A8698"),
	ShakeScreen(amount=5, speed=8),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
	StopShakingObject(),
	ReturnSubroutine(),
	SetAMEM8BitToAbsolute7E(0x60, 0x7EE00E, identifier="command_0x3A86A7"),
	JmpIfAMEM8BitEqualsConst(0x60, 1, ["command_0x3A86DB"]),
	JmpIfAMEM8BitEqualsConst(0x60, 2, ["command_0x3A86EA"]),
	JmpIfAMEM8BitEqualsConst(0x60, 3, ["command_0x3A86F6"]),
	JmpIfAMEM8BitEqualsConst(0x60, 4, ["command_0x3A86FC"]),
	JmpIfAMEM8BitEqualsConst(0x60, 5, ["command_0x3A8708"]),
	JmpIfAMEM8BitEqualsConst(0x60, 6, ["command_0x3A8714"]),
	JmpIfAMEM8BitEqualsConst(0x60, 7, ["command_0x3A8720"]),
	JmpIfAMEM8BitEqualsConst(0x60, 8, ["command_0x3A872C"]),
	ResetTargetMappingMemory(identifier="command_0x3A86DB"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=106, y=92, z=0, set_x=True, set_y=True, set_z=True),
	PlaySound(sound=S0149_ENEMY_JUMPS_HIGH, identifier="command_0x3A86E4"),
	RunSubroutine(["command_0x3A726E"]),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A86EA"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=219, y=114, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A86E4"]),
	RunSubroutine(["command_0x3A82BE"], identifier="command_0x3A86F6"),
	Jmp(["command_0x3A86E4"]),
	ResetTargetMappingMemory(identifier="command_0x3A86FC"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=110, y=80, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A86E4"]),
	ResetTargetMappingMemory(identifier="command_0x3A8708"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=196, y=80, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A86E4"]),
	ResetTargetMappingMemory(identifier="command_0x3A8714"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=220, y=155, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A86E4"]),
	ResetTargetMappingMemory(identifier="command_0x3A8720"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=104, y=121, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A86E4"]),
	ResetTargetMappingMemory(identifier="command_0x3A872C"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=179, y=162, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A86E4"]),
	ScreenFlashWithDuration(WHITE, 1, 16, identifier="command_0x3A8738"),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x64, identifier="command_0x3A873C"),
	SetAMEM8BitToConst(0x64, 1),
	Pause1Frame(identifier="command_0x3A8742"),
	SetAMEMToAMEM8Bit(dest_amem=0x68, upper=0x40, amem=0x68),
	SetAMEMToAMEM8Bit(dest_amem=0x69, upper=0x40, amem=0x69),
	SetAMEMToAMEM8Bit(dest_amem=0x6A, upper=0x40, amem=0x6A),
	SetAMEMToAMEM8Bit(dest_amem=0x6B, upper=0x40, amem=0x6B),
	SetAMEMToAMEM8Bit(dest_amem=0x6C, upper=0x40, amem=0x6C),
	SetAMEMToAMEM8Bit(dest_amem=0x6D, upper=0x40, amem=0x6D),
	SetAMEMToAMEM8Bit(dest_amem=0x6E, upper=0x40, amem=0x6E),
	SetAMEMToAMEM8Bit(dest_amem=0x6F, upper=0x40, amem=0x6F),
	SetAMEMToAMEM8Bit(dest_amem=0x67, upper=0x40, amem=0x64),
	Pause1Frame(),
	DecAMEM8BitByAMEM(amem=0x69, source_amem=0x67, upper=0x60),
	DecAMEM8BitByConst(0x6B, 2),
	IncAMEM8BitByAMEM(amem=0x6D, source_amem=0x67, upper=0x60),
	IncAMEM8BitByConst(0x6F, 4),
	DecAMEM8Bit(0x65),
	JmpIfAMEM8BitEqualsConst(0x65, 0, ["command_0x3A8783"]),
	Jmp(["command_0x3A8742"]),
	ReturnSubroutine(identifier="command_0x3A8783"),
	ClearAMEM8Bit(0x6D, identifier="command_0x3A8784"),
	SetAMEM8BitToConst(0x6D, 1),
	Pause1Frame(identifier="command_0x3A878A"),
	SetAMEMToAMEM8Bit(dest_amem=0x68, upper=0x40, amem=0x6A),
	SetAMEMToAMEM8Bit(dest_amem=0x67, upper=0x40, amem=0x6D),
	IncAMEM8BitByAMEM(amem=0x6A, source_amem=0x6C, upper=0x60),
	JmpIfAMEM8BitGreaterOrEqualThanAMEM(amem=0x6A, source_amem=0x6B, upper=0x60, destinations=["command_0x3A87A0"]),
	Jmp(["command_0x3A878A"]),
	ReturnSubroutine(identifier="command_0x3A87A0")
])
