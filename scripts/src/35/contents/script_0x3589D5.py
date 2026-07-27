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
	Jmp(["command_0x358938"], identifier="extracted_subr_acbe748c25d341b9a000084c05b04a2e"),
	Jmp(["extracted_subr_6fef0b15c8fa4c8381ba917c324ec9f8"]),
	Jmp(["extracted_subr_4c8e7f03898349049d824ebb1906c976"]),
	Jmp(["extracted_subr_d73eb868805a43e4a8268e0571582027"]),
	Jmp(["extracted_subr_bd555067ff88495bbf60e779cb08df80"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0008_TOADSTOOL_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	Jmp(["extracted_subr_b20defeba199431198daba81eb73cf38"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0012_TOADSTOOL_FALLEN_CRYING, sequence=3, store_to_vram=True, overlap_all_sprites=True),
	Jmp(["extracted_subr_747aac09370140cd92e03ca749e65ea5"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0008_TOADSTOOL_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	Jmp(["extracted_subr_cc58151736a34b98aa3c4b1b0884985c"], identifier="extracted_subr_364407a3ba8e4fa2bb535e67a8002dcf"),
	Jmp(["extracted_subr_d73eb868805a43e4a8268e0571582027"])
])
