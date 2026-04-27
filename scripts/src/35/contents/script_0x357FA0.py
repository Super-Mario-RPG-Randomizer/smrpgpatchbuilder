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

script = AnimationScriptBlock(expected_size=66, expected_beginning=0x357FA0, script=[
	ResetTargetMappingMemory(identifier="command_0x357FA0"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=8, y=-20, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_d0ab02e565174427b57f23627a12d02d"]),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x357FB6"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=0, y=0, z=-16, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=256, arch_height=48),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	Jmp(["extracted_subr_da5727cd72e745079d79dcbf57363bbc"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE, identifier="extracted_subr_d3a32d684ac44c6fb6b1cdd0f05c566c"),
	ReturnSubroutine()
])
