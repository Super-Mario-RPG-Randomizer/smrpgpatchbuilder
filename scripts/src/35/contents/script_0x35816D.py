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

script = AnimationScriptBlock(expected_size=258, expected_beginning=0x35816D, script=[
	DefineObjectQueue(["command_0x3581B7", "command_0x3581B9", "command_0x3581B9", "command_0x3581BC", "command_0x3581C1", "command_0x3581BC", "command_0x3581CB", "command_0x3581D0", "command_0x3581B7", "command_0x3581DA", "command_0x3581DC", "command_0x3581DF", "command_0x3581BC", "command_0x3581DF", "command_0x3581BC", "command_0x3581DA", "command_0x3581F8", "command_0x3581FA", "command_0x3581D0", "command_0x358202", "command_0x358207", "command_0x3581BC", "command_0x3581CB", "command_0x35821C", "command_0x358221", "command_0x358226", "command_0x3581DA", "command_0x358236", "command_0x3581BC", "extracted_subr_pos2_d9fc0a4581e34ef3b6b46212269fb4a6", "extracted_subr_pos2_d9fc0a4581e34ef3b6b46212269fb4a6", "command_0x358240", "command_0x358242", "command_0x358245", "command_0x35824A", "command_0x3581BC", "command_0x358251"], identifier="command_0x35816D"),
	PlaySound(sound=S0080_WALLOP_1, identifier="command_0x3581B7"),
	Jmp(["command_0x358251"], identifier="command_0x3581B9"),
	PlaySound(sound=S0054_HAMMER_HIT_1, identifier="command_0x3581BC"),
	Jmp(["command_0x358251"], identifier="extracted_subr_pos2_d9fc0a4581e34ef3b6b46212269fb4a6"),
	PlaySound(sound=S0010_MALLOW_PUNCH_1, identifier="command_0x3581C1"),
	Jmp(["command_0x3581B9"]),
	PlaySound(sound=S0018_SUPER_JUMP_HIT_1, identifier="command_0x3581CB"),
	Jmp(["command_0x358251"]),
	PlaySound(sound=S0059_SUPER_JUMP_HIT_3, identifier="command_0x3581D0"),
	Jmp(["command_0x358251"], identifier="extracted_subr_pos1_39725caa7ec144f1901da762f727ee7c"),
	Jmp(["command_0x3581B7"]),
	PlaySound(sound=S0113_GENO_FINGER_SHOT_HIT, identifier="command_0x3581DA"),
	Jmp(["command_0x358251"], identifier="command_0x3581DC"),
	PlaySound(sound=S0122_POISONED, identifier="command_0x3581DF"),
	Jmp(["command_0x3581B9"]),
	Jmp(["command_0x3581DF"]),
	Jmp(["command_0x3581DA"]),
	PlaySound(sound=S0010_MALLOW_PUNCH_1, identifier="command_0x3581F8"),
	Jmp(["command_0x358251"], identifier="command_0x3581FA"),
	Jmp(["command_0x3581D0"]),
	PlaySound(sound=S0046_PLASMA_BOUNCE, identifier="command_0x358202"),
	Jmp(["command_0x358251"]),
	PlaySound(sound=S0159_BIG_DEEP_HIT, identifier="command_0x358207"),
	Jmp(["command_0x3581B9"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	Jmp(["command_0x3581BC"]),
	Jmp(["command_0x3581CB"]),
	PlaySound(sound=S0137_BOWSER_CRUSH_STOMP, identifier="command_0x35821C"),
	Jmp(["command_0x358251"]),
	PlaySound(sound=S0084_WALLOP_4, identifier="command_0x358221"),
	Jmp(["command_0x358251"]),
	PlaySound(sound=S0160_SLAP, identifier="command_0x358226"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
	PlaySound(sound=S0160_SLAP),
	Jmp(["command_0x358251"], identifier="extracted_subr_74c5bc9742fa42c2a3a688ee95ad0cac"),
	Jmp(["command_0x3581DA"]),
	PlaySound(sound=S0152_HIT, identifier="command_0x358236"),
	Jmp(["command_0x3581B9"]),
	PlaySound(sound=S0197_GENO_STAR_GUN_HIT, identifier="command_0x358240"),
	Jmp(["command_0x358251"], identifier="command_0x358242"),
	PlaySound(sound=S0194_BIG_SHELL_HIT_2, identifier="command_0x358245"),
	Jmp(["command_0x358251"]),
	PlaySound(sound=S0083_FRYING_PAN_HIT_1, identifier="command_0x35824A"),
	Jmp(["command_0x3581B9"]),
	SetAMEM60ToCurrentTarget(identifier="command_0x358251"),
	SetAMEM32ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=4, y=-10, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_afe0e71b87ab4ccdb3392ba05b3b5215"]),
	PauseScriptUntilAMEMBitsSet(0x6F, [0, 1, 2, 3, 4, 5, 6, 7]),
	ResetObjectMappingMemory(identifier="extracted_subr_1aec1b34ed91438bbaafcc4500478b3a"),
	Jmp(["extracted_subr_60794ae2994a4d3c99186ce19dc2c129"]),
])
