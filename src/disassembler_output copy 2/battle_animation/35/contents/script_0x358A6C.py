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

script = AnimationScriptBlock(expected_size=235, expected_beginning=0x358A6C, script=[
	ResetTargetMappingMemory(identifier="command_0x358A6C"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM8BitToConst(0x66, 1),
	SetAbsolute7EToAMEM8Bit(0x7EE020, 0x66),
	SetAMEM8BitToRAMRelative7E(0x66, 0x7E002E),
	JmpIfAMEM8BitEqualsConst(0x66, 20, ["command_0x358A9B"]),
	Pause1Frame(),
	JmpIfAMEM8BitEqualsConst(0x66, 11, ["command_0x358AAD"]),
	JmpIfAMEM8BitEqualsConst(0x66, 13, ["command_0x358AAD"]),
	JmpIfAMEM8BitEqualsConst(0x66, 23, ["command_0x358AAD"]),
	JmpIfAMEM8BitEqualsConst(0x66, 38, ["command_0x358AAD"]),
	ClearAMEM8Bit(0x66),
	UnknownCommand(bytearray([0x44, 0x55])),
	Jmp(["command_0x358AA2"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x358A9B"),
	RunSubroutine(["command_0x35D2DE"]),
	UnknownCommand(bytearray([0x44, 0x6B])),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x358AA2"),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	RunSubroutine(["command_0x352163"]),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E, identifier="command_0x358AAD"),
	ClearAMEM16Bit(0x61),
	ClearAMEM16Bit(0x63),
	ClearAMEM8Bit(0x65),
	ClearAMEM8Bit(0x67),
	SetAMEM8BitToRAMRelative7E(0x6A, 0x7E002E),
	ClearAMEM8Bit(0x6B),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	JmpIfTimedHitSuccess(destinations=["command_0x358B2A"]),
	ClearAMEM8Bit(0x6F),
	JmpIfAMEM8BitEqualsConst(0x66, 0, ["command_0x358AD0"]),
	PauseScriptUntilAMEMBitsSet(0x67, [0]),
	ClearAMEM16Bit(0x60, identifier="command_0x358AD0"),
	UnknownCommand(bytearray([0xDB, 0x6B])),
	UnknownCommand(bytearray([0x81])),
	Pause1Frame(),
	Jmp(["command_0x358AE1"]),
	ClearAMEM16Bit(0x60, identifier="command_0x358AD9"),
	ClearAMEM8Bit(0x6F),
	UnknownCommand(bytearray([0xDB, 0x6F])),
	UnknownCommand(bytearray([0x82])),
	Pause1Frame(),
	SetAMEM8BitToAbsolute7E(0x6F, 0x7EE020, identifier="command_0x358AE1"),
	JmpIfAMEM8BitNotEqualsConst(0x6F, 0, ["command_0x358AF8"]),
	SetAMEM8BitToConst(0x6F, 1),
	SetAbsolute7EToAMEM8Bit(0x7EE025, 0x6F),
	UseSpriteQueue(field_object=0, destinations=["command_0x35F618"], character_slot=True, bit_5=True),
	AttackTimerBegins(identifier="command_0x358AF8"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	UnknownCommand(bytearray([0x3C, 0x00, 0x08])),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToConst(0x65, 1),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0014_BOWSER_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="command_0x358B07"),
	Jmp(["command_0x35898C"]),
	Jmp(["command_0x358991"], identifier="command_0x358B10"),
	ResetTargetMappingMemory(identifier="command_0x358B13"),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x358081"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0018_BOWSER_CAST_SPELL, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	Jmp(["command_0x358B07"]),
	PlaySound(sound=S0172_WEAPON_TIMING, channel=4, identifier="command_0x358B2A"),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E),
	ClearAMEM8Bit(0x61),
	SetAMEM8BitToConst(0x62, 1),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	Jmp(["command_0x358AD9"])
])
