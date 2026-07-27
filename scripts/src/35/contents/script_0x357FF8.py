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

script = AnimationScriptBlock(expected_size=165, expected_beginning=0x357FF8, script=[
	ResetTargetMappingMemory(identifier="command_0x357FF8"),
	MoveObject(speed=1, start_position=-137, end_position=0, apply_to_x=True, should_set_speed=True),
	MoveObject(speed=1, start_position=80, end_position=0, apply_to_y=True, should_set_speed=True),
	Jmp(["extracted_subr_adfe640e410c473090526ceee4af0ad0"]),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x35803B"),
	Jmp(["extracted_subr_9331303645824385ba3dc7b49a94ba6c"]),
	Jmp(["extracted_subr_adfe640e410c473090526ceee4af0ad0"]),
	Jmp(["extracted_subr_260e75ced2b14a81bb9bc3a9ccd673d1"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	Jmp(["extracted_subr_d3a32d684ac44c6fb6b1cdd0f05c566c"]),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x358086"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=12, y=-6, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1664, arch_height=0),
	Jmp(["extracted_subr_4b9e085ffed5427caacbe3036f947505"], identifier="extracted_subr_bd60b6fe10c44dc094c656c08bca27fc"),
	ReturnSubroutine()
])
