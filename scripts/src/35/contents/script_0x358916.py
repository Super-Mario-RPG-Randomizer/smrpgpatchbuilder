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
	ClearAMEM8Bit(0x66, identifier="extracted_subr_16e5c1a5255043eeac572aa7b4551dd6"),
	UnknownCommand(bytearray([0x44, 0x55])),
	Jmp(["command_0x358938"]),
	UnknownCommand(bytearray([0x44, 0x68]), identifier="command_0x358936"),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x358938"),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	Jmp(["extracted_subr_18e35c801dd342daae7651e5955f4857"]),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E, identifier="extracted_subr_pos3_13845169c079474996c0e0e02f4ca2dc"),
	ClearAMEM16Bit(0x61),
	ClearAMEM16Bit(0x63, identifier="extracted_subr_6fef0b15c8fa4c8381ba917c324ec9f8"),
	ClearAMEM8Bit(0x65),
	ClearAMEM8Bit(0x67),
	SetAMEM8BitToRAMRelative7E(0x6A, 0x7E002E, identifier="extracted_subr_4c8e7f03898349049d824ebb1906c976"),
	ClearAMEM8Bit(0x6B),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"], identifier="extracted_subr_cd97bb5b3f994cb9b5405c005fcd3206"),
	JmpIfTimedHitSuccess(destinations=["command_0x3589BF"]),
	ClearAMEM8Bit(0x6F, identifier="extracted_subr_608bf5e4602d4e65bbac8b7762b01df2"),
	JmpIfAMEM8BitEqualsConst(0x66, 0, ["command_0x358968"]),
	PauseScriptUntilAMEMBitsSet(0x67, [0], identifier="extracted_subr_a481a2d157c740c2b9994949ba594269"),
	ClearAMEM16Bit(0x60, identifier="command_0x358968"),
	UnknownCommand(bytearray([0xDB, 0x6B]), identifier="extracted_subr_bd555067ff88495bbf60e779cb08df80"),
	UnknownCommand(bytearray([0x81])),
	Pause1Frame(),
	Jmp(["command_0x358979"]),
	Jmp(["extracted_subr_d73eb868805a43e4a8268e0571582027"], identifier="extracted_subr_6fe6810be3484493965735bf411899b6"),
	UnknownCommand(bytearray([0xDB, 0x6F]), identifier="extracted_subr_6c08a97f5ba842a38ecca9861e6bf6d3"),
	UnknownCommand(bytearray([0x82])),
	Pause1Frame(identifier="extracted_subr_pos3_3912998dbfce4924b74788804f24d43d"),
	AttackTimerBegins(identifier="command_0x358979"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0], identifier="extracted_subr_pos1_680cf2c8f038481088d9d7046edf625a"),
	UnknownCommand(bytearray([0x3C, 0x00, 0x08])),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToConst(0x65, 1),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0002_MARIO_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	Jmp(["extracted_subr_cc58151736a34b98aa3c4b1b0884985c"], identifier="extracted_subr_b20defeba199431198daba81eb73cf38"),
	ResetTargetMappingMemory(identifier="command_0x3589A0"),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x358086"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0006_MARIO_CROUCH_UP_RIGHT, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(identifier="extracted_subr_747aac09370140cd92e03ca749e65ea5"),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0002_MARIO_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["extracted_subr_04f38411c01448c2ba8467a80ad991e9"], identifier="extracted_subr_cc58151736a34b98aa3c4b1b0884985c"),
	UnknownCommand(bytearray([0x6D])),
	ReturnSubroutine(),
	PlaySound(sound=S0172_WEAPON_TIMING, channel=4, identifier="command_0x3589BF"),
	SetAMEM8BitToConst(0x63, 1),
	Jmp(["extracted_subr_b2dc6d61b07744faa046d5c584f99d92"]),
	SetAMEM8BitToConst(0x62, 1),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	Jmp(["extracted_subr_d73eb868805a43e4a8268e0571582027"])
])
