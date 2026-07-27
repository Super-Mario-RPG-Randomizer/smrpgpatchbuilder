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

script = AnimationScriptBlock(expected_size=75, expected_beginning=0x35240C, script=[
	ClearAMEM8Bit(0x6F, identifier="command_0x35240C"),
	SetAMEM16BitToConst(0x60, 17),
	Jmp(["useOQat355F1D_subr"], identifier="extracted_subr_5647bfca4fd24663b754d5a826bb2e71"),
	ClearAMEM8Bit(0x6F, identifier="command_0x35241B"),
	SetAMEM16BitToConst(0x60, 18),
	Jmp(["extracted_subr_5647bfca4fd24663b754d5a826bb2e71"]),
	SetAMEM16BitToConst(0x60, 19),
	Jmp(["extracted_subr_5647bfca4fd24663b754d5a826bb2e71"]),
	SetAMEM16BitToConst(0x60, 20),
	Jmp(["extracted_subr_5647bfca4fd24663b754d5a826bb2e71"]),
	SetAMEM16BitToConst(0x60, 21),
	Jmp(["useOQat355F1D_subr"]),
])
