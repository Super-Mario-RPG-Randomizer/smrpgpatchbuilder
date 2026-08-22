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

script = AnimationScriptBlock(expected_size=0x202, expected_beginning=0x350000, script=[
	DefineObjectQueue(["ally_behaviour_pointers"], identifier="command_0x350000"),
	DefineObjectQueue(["command_0x350402", "command_0x350412", "command_0x350422", "command_0x350432", "command_0x350442", "command_0x350402"], identifier="ally_behaviour_pointers"),

	
    SetAMEM8BitToRAMRelative7E(0x60, 0x7EE006, identifier="CULEXTURNSAttack"),
    JmpIfAMEM8BitEqualsConst(0x60, 0, ["CULEXTURNSAttack_sub"]),
    SetAMEM16BitTo7F(0x64, 0x7FFFA0),
    IncAMEM8Bit(0x64),
    Pause1Frame(),
    Set7FToAMEM8Bit(0x7FFFA0, 0x64),
    ReturnSubroutine(),
    SetAMEM8BitToConst(0x60, 0, identifier="CULEXTURNSAttack_sub"),
    Set7FToAMEM8Bit(0x7FFFA0, 0x60),
    ReturnSubroutine(),
    
])
