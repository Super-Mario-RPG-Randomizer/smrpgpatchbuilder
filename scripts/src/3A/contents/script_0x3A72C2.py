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

script = AnimationScriptBlock(expected_size=102, expected_beginning=0x3A72C2, script=[
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1792, arch_height=0, identifier="command_0x3A72C2"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=2048, arch_height=0, identifier="command_0x3A72CE"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=64, arch_height=0, identifier="command_0x3A72DA"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=48, identifier="command_0x3A72E6"),
	Jmp(["extracted_subr_e73a4b5875af47a98389d0dc2c679440"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=96, identifier="command_0x3A72F1"),
	Jmp(["extracted_subr_e73a4b5875af47a98389d0dc2c679440"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=144, identifier="command_0x3A72FC"),
	Jmp(["extracted_subr_e73a4b5875af47a98389d0dc2c679440"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=192, identifier="command_0x3A7307"),
	Jmp(["extracted_subr_e73a4b5875af47a98389d0dc2c679440"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=240, identifier="command_0x3A7312"),
	Jmp(["extracted_subr_e73a4b5875af47a98389d0dc2c679440"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=288, identifier="command_0x3A731D"),
	Jmp(["extracted_subr_e73a4b5875af47a98389d0dc2c679440"]),
])
