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

script = AnimationScriptBlock(expected_size=76, expected_beginning=0x02F455, script=[
	DefineObjectQueue(["command_0x02F461", "command_0x02F462", "command_0x02F473", "command_0x02F473", "command_0x02F48C", "command_0x02F499"], identifier="command_0x02F455"),
	ReturnSubroutine(identifier="command_0x02F461"),
	InitializeBonusMessageSequence(identifier="command_0x02F462"),
	DisplayBonusMessage(message=BM_ATTACK, x=0, y=-32),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=10, identifier="extracted_subr_bac1b0f2581b4228a2828c6aa8efc0f2"),
	DisplayBonusMessage(message=BM_UP, x=2, y=-24),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine(),
	InitializeBonusMessageSequence(identifier="command_0x02F473"),
	DisplayBonusMessage(message=BM_DEFENSE, x=0, y=-32),
	Jmp(["extracted_subr_bac1b0f2581b4228a2828c6aa8efc0f2"]),
	DisplayBonusMessage(message=BM_HPMAX, x=4, y=-32),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine(),
	InitializeBonusMessageSequence(identifier="command_0x02F48C"),
	DisplayBonusMessage(message=BM_ONCE, x=0, y=-32),
	DisplayBonusMessage(message=BM_AGAIN, x=4, y=-24),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine(),
	InitializeBonusMessageSequence(identifier="command_0x02F499"),
	DisplayBonusMessage(message=BM_LUCKY, x=2, y=-32),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine()
])
