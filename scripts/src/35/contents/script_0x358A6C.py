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
	JmpIfAMEM8BitEqualsConst(0x66, 11, ["extracted_subr_pos3_13845169c079474996c0e0e02f4ca2dc"]),
	JmpIfAMEM8BitEqualsConst(0x66, 13, ["extracted_subr_pos3_13845169c079474996c0e0e02f4ca2dc"]),
	JmpIfAMEM8BitEqualsConst(0x66, 23, ["extracted_subr_pos3_13845169c079474996c0e0e02f4ca2dc"]),
	Jmp(["extracted_subr_16e5c1a5255043eeac572aa7b4551dd6"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x358A9B"),
	SetAbsolute7EToAMEM8Bit(0x7EE020, 0x6F),
	UnknownCommand(bytearray([0x44, 0x6B])),
	Jmp(["extracted_subr_acbe748c25d341b9a000084c05b04a2e"]),
	ClearAMEM8Bit(0x67),
	Jmp(["extracted_subr_4c8e7f03898349049d824ebb1906c976"]),
	Jmp(["extracted_subr_608bf5e4602d4e65bbac8b7762b01df2"]),
	Jmp(["extracted_subr_a481a2d157c740c2b9994949ba594269"]),
	Jmp(["command_0x358AE4"]),
	Jmp(["extracted_subr_6fe6810be3484493965735bf411899b6"]),
	SetAMEM8BitToAbsolute7E(0x6F, 0x7EE020, identifier="command_0x358AE4"),
	JmpIfAMEM8BitNotEqualsConst(0x6F, 0, ["command_0x358979"]),
	SetAMEM8BitToConst(0x6F, 1),
	SetAbsolute7EToAMEM8Bit(0x7EE025, 0x6F),
	UseSpriteQueue(field_object=0, destinations=["command_0x35F72A"], character_slot=True, bit_5=True),
	Jmp(["command_0x358979"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0014_BOWSER_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	Jmp(["extracted_subr_b20defeba199431198daba81eb73cf38"]),
	SetOMEM60To072C(),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C992"]),
	SpriteSequence(sequence=0, looping_off=True),
	Jmp(["extracted_subr_b20defeba199431198daba81eb73cf38"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0018_BOWSER_CAST_SPELL, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	Jmp(["extracted_subr_747aac09370140cd92e03ca749e65ea5"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0014_BOWSER_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	Jmp(["extracted_subr_364407a3ba8e4fa2bb535e67a8002dcf"]),
])
