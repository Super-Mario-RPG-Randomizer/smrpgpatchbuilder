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
	SetAbsolute7EToAMEM8Bit(0x7EE01B, 0x68, identifier="extracted_subr_25d87b6d83434078add9dcaaaaea8e39"),
	ReturnSubroutine(identifier="extracted_subr_pos1_9fdc26f825e84e30a61ab10c91e0993a"),
	Jmp(["command_0x35336F"]),
	SetAMEMBits(0x68, [1]),
	Jmp(["extracted_subr_25d87b6d83434078add9dcaaaaea8e39"]),
	SetAMEMBits(0x68, [2]),
	Jmp(["extracted_subr_25d87b6d83434078add9dcaaaaea8e39"]),
	SetAMEMBits(0x68, [3]),
	Jmp(["extracted_subr_25d87b6d83434078add9dcaaaaea8e39"]),
	SetAMEMBits(0x68, [4]),
	Jmp(["extracted_subr_25d87b6d83434078add9dcaaaaea8e39"]),
	SetAMEMBits(0x68, [5]),
	Jmp(["extracted_subr_25d87b6d83434078add9dcaaaaea8e39"]),
	SetAMEMBits(0x68, [6]),
	Jmp(["extracted_subr_25d87b6d83434078add9dcaaaaea8e39"]),
	SetAMEMBits(0x68, [7]),
	Jmp(["extracted_subr_25d87b6d83434078add9dcaaaaea8e39"]),
	Pause1Frame(identifier="command_0x3533DF"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3533DF"]),
	Jmp(["extracted_subr_pos1_9fdc26f825e84e30a61ab10c91e0993a"]),
	JmpIfAMEMBitsClear(0x68, [1], ["command_0x3533DF"]),
	Jmp(["extracted_subr_pos1_9fdc26f825e84e30a61ab10c91e0993a"]),
	JmpIfAMEMBitsClear(0x68, [2], ["command_0x3533DF"]),
	Jmp(["extracted_subr_pos1_9fdc26f825e84e30a61ab10c91e0993a"]),
	JmpIfAMEMBitsClear(0x68, [3], ["command_0x3533DF"]),
	Jmp(["extracted_subr_pos1_9fdc26f825e84e30a61ab10c91e0993a"]),
	JmpIfAMEMBitsClear(0x68, [4], ["command_0x3533DF"]),
	Jmp(["extracted_subr_pos1_9fdc26f825e84e30a61ab10c91e0993a"]),
	JmpIfAMEMBitsClear(0x68, [5], ["command_0x3533DF"]),
	Jmp(["extracted_subr_pos1_9fdc26f825e84e30a61ab10c91e0993a"]),
	JmpIfAMEMBitsClear(0x68, [6], ["command_0x3533DF"]),
	ReturnSubroutine()
])
