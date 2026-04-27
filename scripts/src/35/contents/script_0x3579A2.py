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

script = AnimationScriptBlock(expected_size=322, expected_beginning=0x3579A2, script=[
	ResetTargetMappingMemory(identifier="command_0x3579A2"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x40])),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=80),
	Jmp(["extracted_subr_fb9412a09b534997a721442c56c64753"], identifier="extracted_subr_c81ebe4daac646039cdeeb06bd5559bc"),
	ResetObjectMappingMemory(identifier="extracted_subr_pos1_6d56384781af4903ab5c284c7e422758"),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x80])),
	SpriteSequence(sequence=3, identifier="extracted_subr_11d041f98e4d4d609a71acaf97a6cc9e"),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=5),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=2048, arch_height=0),
	Jmp(["extracted_subr_c81ebe4daac646039cdeeb06bd5559bc"]),
	Jmp(["extracted_subr_1d8a34b4b2624169ade1812a2ddcc6f5"]),
	MoveObject(speed=-101, start_position=0, end_position=-513, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=5, identifier="extracted_subr_f2c861fa1d3149ecbee819ad33bfeda7"),
	Jmp(["extracted_subr_pos1_6d56384781af4903ab5c284c7e422758"]),
	MoveObject(speed=103, start_position=-513, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	Jmp(["extracted_subr_f2c861fa1d3149ecbee819ad33bfeda7"]),
	ResetSpriteSequence(),
	Jmp(["extracted_subr_260e75ced2b14a81bb9bc3a9ccd673d1"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1280, arch_height=96),
	Jmp(["extracted_subr_8089941b9f9b4ba68ca55bdc0d336043"]),
	ResetTargetMappingMemory(identifier="command_0x357A19"),
	ResetObjectMappingMemory(),
	MoveObject(speed=17, start_position=256, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	MoveObject(speed=25, start_position=-769, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	Jmp(["extracted_subr_01544ce5aa754df994632a0b9d0fc075"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=32, y=-16, z=-32, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1536, arch_height=0),
	PauseScriptUntil(condition=UNKNOWN_PAUSE_4),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x357A4C"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=-16, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_da81412bf218403d8994a6ae20b79fe0"]),
	ResetSpriteSequence(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_a9aac9221ee44d59a07d3b91740acc61"]),
	Jmp(["extracted_subr_086d5a865bdb4c6980038243db25a7e6"]),
	Jmp(["extracted_subr_45babb9c2d9b45dda08e9a43b7215cd8"]),
	SpriteSequence(sequence=5),
	Jmp(["extracted_subr_f088927e00f9479996e65f3386596f57"]),
	Jmp(["extracted_subr_0bf8da0430cb42ec9d639653f0194754"]),
])
