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

script = AnimationScriptBlock(expected_size=29, expected_beginning=0x3AC795, script=[
	RunSubroutine(["command_0x3A7725"], identifier="command_0x3AC795"),
	RemoveObject(),
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=104, y=121, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3AC526"])
])
