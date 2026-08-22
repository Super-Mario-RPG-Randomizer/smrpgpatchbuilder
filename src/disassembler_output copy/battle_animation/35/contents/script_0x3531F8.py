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
	PauseScriptUntilSpriteSequenceDone(),
	Jmp(["command_0x350D0B"]),
	SpriteSequence(sequence=2, identifier="command_0x3531FE"),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=2),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=2),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	Jmp(["command_0x3505D5"]),
	SpriteSequence(sequence=2, identifier="command_0x35320B"),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=2),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=2),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	Jmp(["command_0x350863"]),
	RunSubroutine(["command_0x35322A"], identifier="command_0x353218"),
	Jmp(["command_0x3505D5"]),
	RunSubroutine(["command_0x35326F"], identifier="command_0x35321E"),
	Jmp(["command_0x350863"]),
	RunSubroutine(["command_0x35326F"], identifier="command_0x353224"),
	Jmp(["command_0x350931"]),
	SpriteSequence(sequence=0, mirror=True, identifier="command_0x35322A"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	SpriteSequence(sequence=1, mirror=True),
	RunSubroutine(["command_0x357D34"]),
	PlaySound(sound=S0062_MONSTER_RUN_AWAY),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=22, y=-8, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=128),
	RunSubroutine(["command_0x357EE2"]),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=72, y=-36, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=192),
	RunSubroutine(["command_0x357EE2"]),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=192, y=-96, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=256),
	RunSubroutine(["command_0x357EE2"], identifier="command_0x35326A"),
	UnknownCommand(bytearray([0xD6])),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, mirror=True, identifier="command_0x35326F"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	SpriteSequence(sequence=1, mirror=True),
	RunSubroutine(["command_0x357D34"]),
	PlaySound(sound=S0062_MONSTER_RUN_AWAY),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=100, y=-100, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X04, speed=1280, arch_height=208),
	Jmp(["command_0x35326A"]),
	ClearAMEM8Bit(0x6D, identifier="command_0x35328E"),
	SetAMEM8BitToConst(0x6D, 1),
	Pause1Frame(identifier="command_0x353294"),
	SetAMEMToAMEM8Bit(dest_amem=0x68, upper=0x40, amem=0x6A),
	SetAMEMToAMEM8Bit(dest_amem=0x67, upper=0x40, amem=0x6D),
	IncAMEM8BitByAMEM(amem=0x6A, source_amem=0x6C, upper=0x60),
	JmpIfAMEM8BitGreaterOrEqualThanAMEM(amem=0x6A, source_amem=0x6B, upper=0x60, destinations=["command_0x3532AA"]),
	Jmp(["command_0x353294"]),
	ReturnSubroutine(identifier="command_0x3532AA"),
	ClearAMEM8Bit(0x6D, identifier="command_0x3532AB"),
	SetAMEM8BitToConst(0x6D, 1),
	Pause1Frame(identifier="command_0x3532B1"),
	SetAMEMToAMEM8Bit(dest_amem=0x68, upper=0x40, amem=0x6A),
	SetAMEMToAMEM8Bit(dest_amem=0x67, upper=0x40, amem=0x6D),
	DecAMEM8BitByAMEM(amem=0x6A, source_amem=0x6C, upper=0x60),
	JmpIfAMEM8BitLessThanAMEM(amem=0x6A, source_amem=0x6B, upper=0x60, destinations=["command_0x3532C7"]),
	Jmp(["command_0x3532B1"]),
	ReturnSubroutine(identifier="command_0x3532C7")
])
