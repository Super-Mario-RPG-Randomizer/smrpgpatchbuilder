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
	DefineObjectQueue(["command_0x3581B7", "command_0x3581B9", "command_0x3581B9", "command_0x3581BC", "command_0x3581C1", "command_0x3581C6", "command_0x3581C9", "command_0x3581CE", "command_0x3581D3", "command_0x3581D8", "command_0x3581DA", "command_0x3581DD", "command_0x3581E2", "command_0x3581E5", "command_0x3581E8", "command_0x3581EB", "command_0x3581F0", "command_0x3581F2", "command_0x3581F5", "command_0x3581F8", "command_0x3581FD", "command_0x358202", "command_0x35820B", "command_0x35820E", "command_0x358213", "command_0x358218", "command_0x358222", "command_0x358225", "command_0x35822A", "command_0x35822C", "command_0x35822C", "command_0x35822F", "command_0x358231", "command_0x358234", "command_0x358239", "command_0x35823E", "command_0x358240"], identifier="command_0x35816D"),
	PlaySound(sound=S0080_WALLOP_1, identifier="command_0x3581B7"),
	Jmp(["command_0x358240"], identifier="command_0x3581B9"),
	PlaySound(sound=S0054_HAMMER_HIT_1, identifier="command_0x3581BC"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0010_MALLOW_PUNCH_1, identifier="command_0x3581C1"),
	Jmp(["command_0x358240"]),
	Jmp(["command_0x3581BC"], identifier="command_0x3581C6"),
	PlaySound(sound=S0018_SUPER_JUMP_HIT_1, identifier="command_0x3581C9"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0059_SUPER_JUMP_HIT_3, identifier="command_0x3581CE"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0080_WALLOP_1, identifier="command_0x3581D3"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0113_GENO_FINGER_SHOT_HIT, identifier="command_0x3581D8"),
	Jmp(["command_0x358240"], identifier="command_0x3581DA"),
	PlaySound(sound=S0122_POISONED, identifier="command_0x3581DD"),
	Jmp(["command_0x358240"]),
	Jmp(["command_0x3581BC"], identifier="command_0x3581E2"),
	Jmp(["command_0x3581DD"], identifier="command_0x3581E5"),
	Jmp(["command_0x3581BC"], identifier="command_0x3581E8"),
	PlaySound(sound=S0113_GENO_FINGER_SHOT_HIT, identifier="command_0x3581EB"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0010_MALLOW_PUNCH_1, identifier="command_0x3581F0"),
	Jmp(["command_0x358240"], identifier="command_0x3581F2"),
	Jmp(["command_0x3581CE"], identifier="command_0x3581F5"),
	PlaySound(sound=S0046_PLASMA_BOUNCE, identifier="command_0x3581F8"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0159_BIG_DEEP_HIT, identifier="command_0x3581FD"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0054_HAMMER_HIT_1, identifier="command_0x358202"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	Jmp(["command_0x3581BC"]),
	Jmp(["command_0x3581C9"], identifier="command_0x35820B"),
	PlaySound(sound=S0137_BOWSER_CRUSH_STOMP, identifier="command_0x35820E"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0084_WALLOP_4, identifier="command_0x358213"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0160_SLAP, identifier="command_0x358218"),
	RunSubroutine(["command_0x358117"]),
	PlaySound(sound=S0160_SLAP),
	Jmp(["command_0x358240"]),
	Jmp(["command_0x3581EB"], identifier="command_0x358222"),
	PlaySound(sound=S0152_HIT, identifier="command_0x358225"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0054_HAMMER_HIT_1, identifier="command_0x35822A"),
	Jmp(["command_0x358240"], identifier="command_0x35822C"),
	PlaySound(sound=S0197_GENO_STAR_GUN_HIT, identifier="command_0x35822F"),
	Jmp(["command_0x358240"], identifier="command_0x358231"),
	PlaySound(sound=S0194_BIG_SHELL_HIT_2, identifier="command_0x358234"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0083_FRYING_PAN_HIT_1, identifier="command_0x358239"),
	Jmp(["command_0x358240"]),
	PlaySound(sound=S0054_HAMMER_HIT_1, identifier="command_0x35823E"),
	SetAMEM60ToCurrentTarget(identifier="command_0x358240"),
	SetAMEM32ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=4, y=-10, z=0, set_x=True, set_y=True, set_z=True),
	RunSubroutine(["command_0x3523A0"]),
	ResetObjectMappingMemory(identifier="command_0x35824C"),
	Jmp(["command_0x352524"])
])
