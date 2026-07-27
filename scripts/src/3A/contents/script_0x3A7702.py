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

script = AnimationScriptBlock(expected_size=347, expected_beginning=0x3A7702, script=[
	Jmp(["command_0x3A764C"]),
	SetAMEMBits(0x68, [6]),
	Jmp(["extracted_subr_b881aa8aa6a9429cb892da33b65d2533"]),
	SetAMEMBits(0x68, [7]),
	Jmp(["extracted_subr_b881aa8aa6a9429cb892da33b65d2533"]),
	Pause1Frame(identifier="command_0x3A771E"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01F),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3A771E"]),
	Jmp(["extracted_subr_pos1_2c3f553eb8894768ad5d80227b17ac27"]),
	JmpIfAMEMBitsClear(0x68, [1], ["command_0x3A771E"]),
	Jmp(["extracted_subr_pos1_2c3f553eb8894768ad5d80227b17ac27"]),
	JmpIfAMEMBitsClear(0x68, [2], ["command_0x3A771E"]),
	Jmp(["extracted_subr_pos1_2c3f553eb8894768ad5d80227b17ac27"]),
	JmpIfAMEMBitsClear(0x68, [3], ["command_0x3A771E"]),
	Jmp(["extracted_subr_pos1_2c3f553eb8894768ad5d80227b17ac27"]),
	JmpIfAMEMBitsClear(0x68, [4], ["command_0x3A771E"]),
	Jmp(["extracted_subr_pos1_2c3f553eb8894768ad5d80227b17ac27"]),
	JmpIfAMEMBitsClear(0x68, [5], ["command_0x3A771E"]),
	Jmp(["extracted_subr_pos1_2c3f553eb8894768ad5d80227b17ac27"]),
	JmpIfAMEMBitsClear(0x68, [6], ["command_0x3A771E"]),
	Jmp(["extracted_subr_pos1_2c3f553eb8894768ad5d80227b17ac27"]),
	JmpIfAMEMBitsClear(0x68, [7], ["command_0x3A771E"]),
	ReturnSubroutine(identifier="extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"),
	Pause1Frame(identifier="command_0x3A7776"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01E),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3A7776"]),
	Jmp(["extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"]),
	JmpIfAMEMBitsClear(0x68, [1], ["command_0x3A7776"]),
	Jmp(["extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"]),
	JmpIfAMEMBitsClear(0x68, [2], ["command_0x3A7776"]),
	Jmp(["extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"]),
	JmpIfAMEMBitsClear(0x68, [3], ["command_0x3A7776"]),
	Jmp(["extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"]),
	JmpIfAMEMBitsClear(0x68, [4], ["command_0x3A7776"]),
	Jmp(["extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"]),
	JmpIfAMEMBitsClear(0x68, [5], ["command_0x3A7776"]),
	Jmp(["extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"]),
	JmpIfAMEMBitsClear(0x68, [6], ["command_0x3A7776"]),
	Jmp(["extracted_subr_edea632ffdda48dfaf8809cd1cd57a1c"]),
	JmpIfAMEMBitsClear(0x68, [7], ["command_0x3A7776"]),
	ReturnSubroutine(identifier="extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"),
	Pause1Frame(identifier="command_0x3A77CE"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01D),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3A77CE"]),
	Jmp(["extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"]),
	JmpIfAMEMBitsClear(0x68, [1], ["command_0x3A77CE"]),
	Jmp(["extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"]),
	JmpIfAMEMBitsClear(0x68, [2], ["command_0x3A77CE"]),
	Jmp(["extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"]),
	JmpIfAMEMBitsClear(0x68, [3], ["command_0x3A77CE"]),
	Jmp(["extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"]),
	JmpIfAMEMBitsClear(0x68, [4], ["command_0x3A77CE"]),
	Jmp(["extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"]),
	JmpIfAMEMBitsClear(0x68, [5], ["command_0x3A77CE"]),
	Jmp(["extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"]),
	JmpIfAMEMBitsClear(0x68, [6], ["command_0x3A77CE"]),
	Jmp(["extracted_subr_406a2f7b51cf40c1aeb89ab3276863c0"]),
	JmpIfAMEMBitsClear(0x68, [7], ["command_0x3A77CE"]),
	ReturnSubroutine(identifier="extracted_subr_70a27e126d18462d82b22387bfd65f72"),
	Pause1Frame(identifier="command_0x3A7826"),
	SetAMEM8BitToAbsolute7E(0x68, 0x7EE01C),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3A7826"]),
	Jmp(["extracted_subr_70a27e126d18462d82b22387bfd65f72"]),
	JmpIfAMEMBitsClear(0x68, [1], ["command_0x3A7826"]),
	Jmp(["extracted_subr_70a27e126d18462d82b22387bfd65f72"]),
	JmpIfAMEMBitsClear(0x68, [2], ["command_0x3A7826"]),
	Jmp(["extracted_subr_70a27e126d18462d82b22387bfd65f72"]),
	JmpIfAMEMBitsClear(0x68, [3], ["command_0x3A7826"]),
	Jmp(["extracted_subr_70a27e126d18462d82b22387bfd65f72"]),
	JmpIfAMEMBitsClear(0x68, [4], ["command_0x3A7826"]),
	ReturnSubroutine()
])
