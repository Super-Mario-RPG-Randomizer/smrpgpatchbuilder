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

script = AnimationScriptBlock(expected_size=151, expected_beginning=0x3589D5, script=[
	ResetTargetMappingMemory(identifier="command_0x3589D5"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x55])),
	SpriteSequence(sequence=0, looping_off=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	RunSubroutine(["command_0x352163"]),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E),
	ClearAMEM16Bit(0x61),
	ClearAMEM16Bit(0x63),
	ClearAMEM8Bit(0x65),
	SetAMEM8BitToRAMRelative7E(0x6A, 0x7E002E),
	ClearAMEM8Bit(0x6B),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	JmpIfTimedHitSuccess(destinations=["command_0x358A40"]),
	ClearAMEM16Bit(0x60),
	ClearAMEM8Bit(0x6F),
	UnknownCommand(bytearray([0xDB, 0x6B])),
	UnknownCommand(bytearray([0x81])),
	Pause1Frame(),
	Jmp(["command_0x358A0E"]),
	ClearAMEM16Bit(0x60, identifier="command_0x358A06"),
	ClearAMEM8Bit(0x6F),
	UnknownCommand(bytearray([0xDB, 0x6F])),
	UnknownCommand(bytearray([0x82])),
	Pause1Frame(),
	AttackTimerBegins(identifier="command_0x358A0E"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	UnknownCommand(bytearray([0x3C, 0x00, 0x08])),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToConst(0x65, 1),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0008_TOADSTOOL_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="command_0x358A1D"),
	Jmp(["command_0x35898C"]),
	Jmp(["command_0x358991"], identifier="command_0x358A26"),
	ResetTargetMappingMemory(identifier="command_0x358A29"),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x358081"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0012_TOADSTOOL_FALLEN_CRYING, sequence=3, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	Jmp(["command_0x358A1D"]),
	PlaySound(sound=S0172_WEAPON_TIMING, channel=4, identifier="command_0x358A40"),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E),
	ClearAMEM8Bit(0x61),
	SetAMEM8BitToConst(0x62, 1),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	Jmp(["command_0x358A06"])
])
