#A0294_EMPTY

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
	A_ToggleSubroutineSlots(0x03),
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x00, 0x6F, 0x00, 0x01, 0xF2, 0xFF, 0x00, 0xFF, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xE0, 0x00, 0x7F, 0x00, 0x01, 0xF2, 0xFF, 0x00, 0xFF, 0x80])),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpSteps(6),
	A_Pause(240),
	A_SetVarToConst(PRIMARY_TEMP_700C, 255),
	A_UnknownCommand(bytearray([0x35, 0x00, 0x04])),
	A_UnknownCommand(bytearray([0x35, 0x01, 0x04])),
	A_Pause(420),
	A_BPL262728(),
	A_ReturnQueue()
])
