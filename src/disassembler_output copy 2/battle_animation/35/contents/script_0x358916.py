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

script = AnimationScriptBlock(expected_size=191, expected_beginning=0x358916, script=[
	ResetTargetMappingMemory(identifier="command_0x358916"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM8BitToRAMRelative7E(0x66, 0x7E002E),
	JmpIfAMEM8BitEqualsConst(0x66, 7, ["command_0x358936"]),
	JmpIfAMEM8BitEqualsConst(0x66, 18, ["command_0x358936"]),
	JmpIfAMEM8BitEqualsConst(0x66, 33, ["command_0x358936"]),
	ClearAMEM8Bit(0x66),
	UnknownCommand(bytearray([0x44, 0x55])),
	Jmp(["command_0x358938"]),
	UnknownCommand(bytearray([0x44, 0x68]), identifier="command_0x358936"),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x358938"),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	RunSubroutine(["command_0x352163"]),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E),
	ClearAMEM16Bit(0x61),
	ClearAMEM16Bit(0x63),
	ClearAMEM8Bit(0x65),
	ClearAMEM8Bit(0x67),
	SetAMEM8BitToRAMRelative7E(0x6A, 0x7E002E),
	ClearAMEM8Bit(0x6B),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	JmpIfTimedHitSuccess(destinations=["command_0x3589B3"]),
	ClearAMEM8Bit(0x6F),
	JmpIfAMEM8BitEqualsConst(0x66, 0, ["command_0x358966"]),
	PauseScriptUntilAMEMBitsSet(0x67, [0]),
	ClearAMEM16Bit(0x60, identifier="command_0x358966"),
	UnknownCommand(bytearray([0xDB, 0x6B])),
	UnknownCommand(bytearray([0x81])),
	Pause1Frame(),
	Jmp(["command_0x358977"]),
	ClearAMEM16Bit(0x60, identifier="command_0x35896F"),
	ClearAMEM8Bit(0x6F),
	UnknownCommand(bytearray([0xDB, 0x6F])),
	UnknownCommand(bytearray([0x82])),
	Pause1Frame(),
	AttackTimerBegins(identifier="command_0x358977"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	UnknownCommand(bytearray([0x3C, 0x00, 0x08])),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToConst(0x65, 1),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0002_MARIO_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="command_0x358986"),
	RunSubroutine(["command_0x35806F"], identifier="command_0x35898C"),
	UnknownCommand(bytearray([0x6D])),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358991"),
	ResetObjectMappingMemory(),
	SetOMEM60To072C(),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C992"]),
	SpriteSequence(sequence=0, looping_off=True),
	Jmp(["command_0x35898C"]),
	ResetTargetMappingMemory(identifier="command_0x35899C"),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x358081"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0006_MARIO_CROUCH_UP_RIGHT, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	Jmp(["command_0x358986"]),
	PlaySound(sound=S0172_WEAPON_TIMING, channel=4, identifier="command_0x3589B3"),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E),
	ClearAMEM8Bit(0x61),
	SetAMEM8BitToConst(0x62, 1),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	Jmp(["command_0x35896F"])
])
