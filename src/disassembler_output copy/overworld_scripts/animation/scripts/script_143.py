#A0143_EMPTY

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
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_VisibilityOn(),
	A_BPL262728(),
	A_ToggleSubroutineSlots(0x03),
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x00, 0x7F, 0xFF, 0x00, 0xE0, 0xFF, 0x00, 0xFE, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xE0, 0x00, 0x5F, 0xFF, 0x00, 0xE0, 0xFF, 0x00, 0xFE, 0x80])),
	A_Pause(58),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
	A_Pause(52),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(52),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(12),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
	A_Pause(48),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(12),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(48),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(60),
	A_Pause(70),
	A_BPL262728(),
	A_ReturnQueue()
])
