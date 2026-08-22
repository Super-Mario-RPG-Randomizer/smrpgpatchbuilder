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

script = AnimationScriptBlock(expected_size=183, expected_beginning=0x3580B4, script=[
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580B4"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=112, y=155, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96, identifier="command_0x3580BE"),
	Jmp(["command_0x358091"]),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580C7"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=96, y=163, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3580BE"]),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580D4"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x68])),
	Jmp(["command_0x3580BE"]),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580DD"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=-52, y=26, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3580BE"]),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580EC"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=44, y=199, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["command_0x3580BE"]),
	SpriteSequence(sequence=4, identifier="command_0x3580FB"),
	PauseScriptUntilSpriteSequenceDone(),
	ReturnSubroutine(),
	SetAMEMToRandomShort(amem=0x60, upper_bound=8, identifier="command_0x3580FF"),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x358107"]),
	ReturnSubroutine(),
	DefineObjectQueue(["command_0x358117", "command_0x35811C", "command_0x358121", "command_0x358126", "command_0x35812B", "command_0x358130", "command_0x358135", "command_0x35813A"], identifier="command_0x358107"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3, identifier="command_0x358117"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=6, identifier="command_0x35811C"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=9, identifier="command_0x358121"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=12, identifier="command_0x358126"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=15, identifier="command_0x35812B"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=18, identifier="command_0x358130"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=21, identifier="command_0x358135"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=24, identifier="command_0x35813A"),
	ReturnSubroutine()
])
