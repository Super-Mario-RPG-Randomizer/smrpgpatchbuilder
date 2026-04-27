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

script = AnimationScriptBlock(expected_size=561, expected_beginning=0x35C761, script=[
	DefineObjectQueue(["command_0x35C803", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C803", "command_0x35C892", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C80E", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CE", "command_0x35C803", "command_0x35C803", "command_0x35C803", "command_0x35C803", "command_0x35C8FE", "command_0x35C8CD", "command_0x35C8CE", "command_0x35C907", "command_0x35C8CE", "extracted_subr_5a80ef945e834cc48aefafa873cb6357", "extracted_subr_5a80ef945e834cc48aefafa873cb6357", "extracted_subr_5a80ef945e834cc48aefafa873cb6357", "command_0x35C803", "command_0x35C91B", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C8CE", "command_0x35C924", "command_0x35C924", "command_0x35C924", "command_0x35C924", "command_0x35C924", "command_0x35C924", "command_0x35C925", "command_0x35C80E", "command_0x35C8CE", "command_0x35C924", "command_0x35C924", "command_0x35C925", "extracted_subr_d76b4580ae55455c8ee47511b54ec517", "extracted_subr_d76b4580ae55455c8ee47511b54ec517", "extracted_subr_d76b4580ae55455c8ee47511b54ec517", "extracted_subr_d76b4580ae55455c8ee47511b54ec517", "command_0x35C80E", "command_0x35C803", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C8CD", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C955", "command_0x35C803", "command_0x35C8CE"], identifier="command_0x35C761"),
	SetAbsolute7EToAMEM16Bit(0x7EE022, 0x60, identifier="command_0x35C803"),
	RunSubroutine(["extracted_subr_7aafe72f5c6847c98ccd728959e1c732"], identifier="extracted_subr_1583c264ad6748f180ae3953abb91cdc"),
	RunSubroutine(["command_0x35C968"], identifier="extracted_subr_d19eecf345b44f8584982d529bdf0a74"),
	ReturnSubroutine(identifier="extracted_subr_d76b4580ae55455c8ee47511b54ec517"),
	SetAbsolute7EToAMEM16Bit(0x7EE022, 0x60, identifier="command_0x35C80E"),
	Jmp(["extracted_subr_1583c264ad6748f180ae3953abb91cdc"]),
	RunSubroutine(["command_0x35C968"]),
	Jmp(["extracted_subr_d76b4580ae55455c8ee47511b54ec517"]),
	RunSubroutine(["extracted_subr_bd94f26b55f54cf1940058067d956c42"]),
	RunSubroutine(["command_0x35C975"]),
	ReturnSubroutine(identifier="extracted_subr_5a80ef945e834cc48aefafa873cb6357"),
	Jmp(["command_0x35C803"]),
	RunSubroutine(["extracted_subr_7aafe72f5c6847c98ccd728959e1c732"], identifier="command_0x35C892"),
	Jmp(["extracted_subr_d76b4580ae55455c8ee47511b54ec517"]),
	RunSubroutine(["extracted_subr_7aafe72f5c6847c98ccd728959e1c732"]),
	RunSubroutine(["command_0x35C975"]),
	Jmp(["extracted_subr_d76b4580ae55455c8ee47511b54ec517"]),
	Jmp(["extracted_subr_1583c264ad6748f180ae3953abb91cdc"]),
	Jmp(["extracted_subr_d19eecf345b44f8584982d529bdf0a74"]),
	ReturnSubroutine(identifier="command_0x35C8CD"),
	RunSubroutine(["extracted_subr_7aafe72f5c6847c98ccd728959e1c732"], identifier="command_0x35C8CE"),
	Jmp(["extracted_subr_5a80ef945e834cc48aefafa873cb6357"], identifier="extracted_subr_d7f52d6b808d4eb4bf3f007bc98936f2"),
	Jmp(["command_0x35C803"]),
	RunSubroutine(["command_0x35C975"]),
	Jmp(["extracted_subr_d7f52d6b808d4eb4bf3f007bc98936f2"]),
	RunSubroutine(["extracted_subr_7aafe72f5c6847c98ccd728959e1c732"], identifier="command_0x35C8FE"),
	ReturnSubroutine(),
	Jmp(["command_0x35C8CD"]),
	RunSubroutine(["command_0x3523DF"], identifier="command_0x35C907"),
	Jmp(["command_0x35C8CD"]),
	Jmp(["extracted_subr_5a80ef945e834cc48aefafa873cb6357"]),
	ReturnSubroutine(identifier="command_0x35C91B"),
	RunSubroutine(["command_0x35CEEF"], identifier="command_0x35C955"),
	Jmp(["command_0x35C8CD"], identifier="extracted_subr_d36e6994ba4f4d89877974ba0fc2918f"),
	ReturnSubroutine(identifier="command_0x35C924"),
	RunSubroutine(["command_0x3523DF"], identifier="command_0x35C925"),
	Jmp(["extracted_subr_d76b4580ae55455c8ee47511b54ec517"], identifier="extracted_subr_7df5868cc4834c74894f144c45affc3e"),
	RunSubroutine(["command_0x3523DF"]),
	RunSubroutine(["command_0x35C968"]),
	Jmp(["extracted_subr_d36e6994ba4f4d89877974ba0fc2918f"]),
	ReturnSubroutine(),
	Jmp(["extracted_subr_7df5868cc4834c74894f144c45affc3e"]),
	Jmp(["extracted_subr_5a80ef945e834cc48aefafa873cb6357"]),
	Jmp(["command_0x35C8CD"]),
	SetAMEMToRandomByte(amem=0x6E, upper_bound=100, identifier="command_0x35C968"),
	JmpIfAMEM8BitGreaterOrEqualThanConst(0x6E, 26, ["command_0x35C974"]),
	RunSubroutine(["command_0x35C982"], identifier="extracted_subr_f9b965ebf2aa44fb931350074ec852c0"),
	ReturnSubroutine(identifier="command_0x35C974"),
	SetAMEMToRandomByte(amem=0x6E, upper_bound=100, identifier="command_0x35C975"),
	JmpIfAMEM8BitGreaterOrEqualThanConst(0x6E, 13, ["command_0x35C974"]),
	Jmp(["extracted_subr_f9b965ebf2aa44fb931350074ec852c0"]),
	PlaySound(sound=S0006_BONUS_FLOWER_STATUS_UP, identifier="command_0x35C982"),
	DisplayMessage(ITEM_NAME, 8),
	PauseScriptUntilDialogClosed(),
	SetAMEM16BitToAbsolute7E(0x60, 0x7EE022),
	IncAMEM16BitByConst(0x60, 96),
	StoreOMEM60ToItemInventory(),
	ReturnSubroutine()
])
