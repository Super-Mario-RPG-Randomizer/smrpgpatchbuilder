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

script = AnimationScriptBlock(expected_size=149, expected_beginning=0x358B57, script=[
	ResetTargetMappingMemory(identifier="command_0x358B57"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x68])),
	Jmp(["command_0x358938"]),
	ClearAMEM8Bit(0x63),
	ClearAMEM8Bit(0x66),
	Jmp(["extracted_subr_4c8e7f03898349049d824ebb1906c976"]),
	ClearAMEM8Bit(0x6F, identifier="extracted_subr_1597fde961464e36b329e189ccdedddd"),
	PauseScriptUntilAMEMBitsSet(0x66, [0]),
	Jmp(["command_0x358968"]),
	Jmp(["extracted_subr_1597fde961464e36b329e189ccdedddd"]),
	ClearAMEM16Bit(0x60),
	Jmp(["extracted_subr_6c08a97f5ba842a38ecca9861e6bf6d3"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0026_GENO_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	Jmp(["extracted_subr_b20defeba199431198daba81eb73cf38"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0030_GENO_MORPH_INTO_CANNON, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	Jmp(["extracted_subr_747aac09370140cd92e03ca749e65ea5"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0026_GENO_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	Jmp(["extracted_subr_cc58151736a34b98aa3c4b1b0884985c"]),
	Jmp(["extracted_subr_1597fde961464e36b329e189ccdedddd"])
])
