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

script = AnimationScriptBlock(expected_size=33, expected_beginning=0x3A7531, script=[
	ClearAMEM8Bit(0x68, identifier="command_0x3A7531"),
	RunSubroutine(["command_0x3A768B"]),
	RunSubroutine(["command_0x3A7629"]),
	RunSubroutine(["command_0x3A75C7"]),
	SetAbsolute7EToAMEM8Bit(0x7EE01F, 0x68, identifier="command_0x3A753C"),
	ReturnSubroutine(),
	SetAMEM8BitToAMEM(amem=0x60, source_amem=0x60, upper=0x50, identifier="command_0x3A7541"),
	ClearAMEMBits(0x60, [6]),
	SetAMEMToAMEM8Bit(dest_amem=0x60, upper=0x50, amem=0x60),
	ReturnSubroutine(),
	UnknownCommand(bytearray([0xA0]), identifier="command_0x3A754D"),
	ReturnObjectQueue()
])
