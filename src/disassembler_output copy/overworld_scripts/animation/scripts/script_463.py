#A0463_FACTORY_SWITCH_ROOM_AMEBOID

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_ShadowOn(),
	A_VisibilityOff(),
	A_Pause(64),
	A_VisibilityOn(),
	A_SetWalkingSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_WalkSouthwestSteps(6),
	A_WalkSouthwestPixels(10),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_FloatingOn(),
	A_JumpToHeight(0),
	A_ShadowOff(),
	A_Pause(24),
	A_SetWalkingSpeed(NORMAL),
	A_ToggleSubroutineSlots(0x07),
	A_SetSubroutineXTargets(512, 512),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(64384, 65136, identifier="ACTION_463_set_subroutine_x_targets_18"),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(256, 896),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(64640, 65136),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_BPL262728(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=17, y=92),
	A_Pause(16),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_ToggleSubroutineSlots(0x07),
	A_SetSubroutineXTargets(896, 400),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(65280, 64768),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(1152, 400),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(32),
	A_BPL262728(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=23, y=91),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_ToggleSubroutineSlots(0x07),
	A_Jmp(["ACTION_463_set_subroutine_x_targets_18"])
])
