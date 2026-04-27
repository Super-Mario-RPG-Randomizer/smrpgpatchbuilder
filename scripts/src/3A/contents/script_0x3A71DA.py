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

script = AnimationScriptBlock(expected_size=220, expected_beginning=0x3A71DA, script=[
	Jmp(["command_0x3A711F"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=64),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE, identifier="extracted_subr_e73a4b5875af47a98389d0dc2c679440"),
	ReturnSubroutine(),
	Jmp(["command_0x3A711F"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=256, arch_height=0, identifier="extracted_subr_0e5edeb9447c4411aa319e54e4c7cade"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"], identifier="extracted_subr_23bd8455affa470db445304eb1f017ab"),
	ResetTargetMappingMemory(identifier="command_0x3A7203"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=32, y=-16, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_0e5edeb9447c4411aa319e54e4c7cade"], identifier="extracted_subr_aed2596412f84b9d9733d7337dc5618b"),
	Jmp(["command_0x3A7203"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=64, identifier="extracted_subr_b262c40f7ff3477f8f3c6bf8e5d1be8f"),
	Jmp(["extracted_subr_23bd8455affa470db445304eb1f017ab"]),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=-32, y=16, z=0, set_x=True, set_y=True, set_z=True, identifier="extracted_subr_pos1_70ccdeb2450845ffbf6b158167c78de0"),
	Jmp(["extracted_subr_aed2596412f84b9d9733d7337dc5618b"]),
	Jmp(["extracted_subr_b262c40f7ff3477f8f3c6bf8e5d1be8f"]),
	MoveObject(speed=1, start_position=-257, end_position=256, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=128, end_position=128, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=65, start_position=-1025, end_position=1024, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4, identifier="extracted_subr_07a11b754c1745e58000f8d0477dcf73"),
	PauseScriptUntil(condition=BUTTON_PRESSED, identifier="extracted_subr_f75b66aa68fb4fa29ffcfe5d2ab51b5d"),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	Jmp(["extracted_subr_0e5edeb9447c4411aa319e54e4c7cade"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=512, arch_height=0, identifier="command_0x3A7286"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=768, arch_height=0, identifier="command_0x3A7292"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1024, arch_height=0, identifier="command_0x3A729E"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1280, arch_height=0, identifier="command_0x3A72AA"),
	Jmp(["extracted_subr_53e07645ee8e43a3adf00d33cc948f36"]),
])
