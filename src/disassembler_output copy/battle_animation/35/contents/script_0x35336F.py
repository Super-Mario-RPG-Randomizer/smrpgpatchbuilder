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

script = AnimationScriptBlock(expected_size=189, expected_beginning=0x35336F, script=[
	ClearAMEM8Bit(0x68, identifier="command_0x35336F"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [0]),
	SetAbsolute7EToAMEM8Bit(0x7EE01B, 0x68, identifier="command_0x353378"),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x35337D"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [1]),
	Jmp(["command_0x353378"]),
	ClearAMEM8Bit(0x68, identifier="command_0x353389"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [2]),
	Jmp(["command_0x353378"]),
	ClearAMEM8Bit(0x68, identifier="command_0x353395"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [3]),
	Jmp(["command_0x353378"]),
	ClearAMEM8Bit(0x68, identifier="command_0x3533A1"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [4]),
	Jmp(["command_0x353378"]),
	ClearAMEM8Bit(0x68, identifier="command_0x3533AD"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [5]),
	Jmp(["command_0x353378"]),
	ClearAMEM8Bit(0x68, identifier="command_0x3533B9"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [6]),
	Jmp(["command_0x353378"]),
	ClearAMEM8Bit(0x68, identifier="command_0x3533C5"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [7]),
	Jmp(["command_0x353378"]),
	Pause1Frame(identifier="command_0x3533D1"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3533D1"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3533DC"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [1], ["command_0x3533DC"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3533E7"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [2], ["command_0x3533E7"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3533F2"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [3], ["command_0x3533F2"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3533FD"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [4], ["command_0x3533FD"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x353408"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [5], ["command_0x353408"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x353413"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [6], ["command_0x353413"]),
	ReturnSubroutine()
])
