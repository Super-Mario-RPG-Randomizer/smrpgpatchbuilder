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

script = AnimationScriptBlock(expected_size=159, expected_beginning=0x357C57, script=[
	MoveObject(speed=17, start_position=-257, end_position=256, apply_to_z=True, should_set_speed=True, identifier="command_0x357C57"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	MoveObject(speed=17, start_position=256, end_position=256, apply_to_z=True, should_set_speed=True),
	PauseScriptUntil(condition=BUTTON_PRESSED),
	ShakeScreen(amount=5, speed=8),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	StopShakingObject(),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x357C7D"),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x48])),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=128),
	RunSubroutine(["command_0x352163"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0001_MARIO_JUMP_FRONT, sequence=3, store_to_vram=True, store_palette=True, overlap_all_sprites=True, bit_4=True),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=0, y=-24, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=128),
	RunSubroutine(["command_0x357EE2"]),
	SpriteSequence(sequence=5, looping_off=True),
	MoveObject(speed=65, start_position=-1025, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	RunSubroutine(["command_0x357D34"]),
	MoveObject(speed=65, start_position=0, end_position=1024, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	Jmp(["command_0x357B6A"]),
	SpriteSequence(sequence=7, looping_off=True, mirror=True, identifier="command_0x357CBC"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=32, y=-16, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=128),
	RunSubroutine(["command_0x358091"]),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1536, arch_height=80),
	RunSubroutine(["command_0x357A67"]),
	ResetObjectMappingMemory(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0000_MARIO_WALKING_DOWN_LEFT, sequence=0, store_to_vram=True, looping=True, store_palette=True, overlap_all_sprites=True),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
