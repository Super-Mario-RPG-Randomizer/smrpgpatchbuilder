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
	Jmp(["command_0x3523BF"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x352415"),
	SetAMEM16BitToConst(0x60, 18),
	Jmp(["command_0x3523BF"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x35241E"),
	SetAMEM16BitToConst(0x60, 19),
	Jmp(["command_0x3523BF"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x352427"),
	SetAMEM16BitToConst(0x60, 20),
	Jmp(["command_0x3523BF"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x352430"),
	SetAMEM16BitToConst(0x60, 21),
	Jmp(["command_0x3523BF"])
])
