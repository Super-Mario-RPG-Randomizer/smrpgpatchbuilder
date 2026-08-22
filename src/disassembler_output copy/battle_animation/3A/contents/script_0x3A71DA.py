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
	ResetTargetMappingMemory(identifier="command_0x3A71DA"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=64),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE, identifier="command_0x3A71E9"),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A71EE"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=256, arch_height=0, identifier="command_0x3A71F7"),
	Jmp(["command_0x3A7157"]),
	ResetTargetMappingMemory(identifier="command_0x3A7200"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=32, y=-16, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A71F7"]),
	ResetTargetMappingMemory(identifier="command_0x3A720C"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=32, y=-16, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=64, identifier="command_0x3A7215"),
	Jmp(["command_0x3A7157"]),
	ResetTargetMappingMemory(identifier="command_0x3A721E"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=-32, y=16, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A71F7"]),
	ResetTargetMappingMemory(identifier="command_0x3A722A"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=-32, y=16, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3A7215"]),
	ResetTargetMappingMemory(identifier="command_0x3A7236"),
	MoveObject(speed=1, start_position=-257, end_position=256, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=128, end_position=128, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=65, start_position=-1025, end_position=1024, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4, identifier="command_0x3A724F"),
	PauseScriptUntil(condition=BUTTON_PRESSED, identifier="command_0x3A7253"),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	Jmp(["command_0x3A71F7"], identifier="command_0x3A7259"),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=512, arch_height=0, identifier="command_0x3A725C"),
	Jmp(["command_0x3A7157"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=768, arch_height=0, identifier="command_0x3A7265"),
	Jmp(["command_0x3A7157"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1024, arch_height=0, identifier="command_0x3A726E"),
	Jmp(["command_0x3A7157"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1280, arch_height=0, identifier="command_0x3A7277"),
	Jmp(["command_0x3A7157"])
])
