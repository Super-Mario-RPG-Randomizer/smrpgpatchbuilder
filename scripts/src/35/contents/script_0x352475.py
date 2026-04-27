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

script = AnimationScriptBlock(expected_size=245, expected_beginning=0x352475, script=[
	Jmp(["extracted_subr_5f9f2670bb864a7ab68b366c9d757ebf"]),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=2, destinations=["command_0x353706"]),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=4, destinations=["command_0x353706"]),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=6, destinations=["command_0x353706"]),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=8, destinations=["command_0x353706"]),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	Jmp(["extracted_subr_3df07c72747647e99990cb6ec06ef0a8"]),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=12, destinations=["command_0x353706"]),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	PlaySound(sound=S0125_SPIKE_SHOT),
	Jmp(["extracted_subr_cbcc93662e9c462b9c98e3f322b5d076"]),
	PlaySound(sound=S0125_SPIKE_SHOT),
	Jmp(["extracted_subr_e7036876a25943a5810e5337ad55d34f"]),
	PlaySound(sound=S0125_SPIKE_SHOT),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=10, destinations=["command_0x353706"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8, identifier="command_0x3524DF"),
	SpriteSequence(sequence=3),
	Jmp(["extracted_subr_5f9f2670bb864a7ab68b366c9d757ebf"]),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=2, destinations=["command_0x353706"], identifier="extracted_subr_d0683c61b0974564879ab23d11c91961"),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=4, destinations=["command_0x353706"]),
	PlaySound(sound=S0175_DEATHSICKLE),
	PauseScriptUntilSpriteSequenceDone(),
	Jmp(["subr_pause_6F.0"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x3524FB"),
	PlaySound(sound=S0051_FIRE_THROW_BIG),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=10, destinations=["command_0x353706"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=15, identifier="extracted_subr_1b2d8b1adca04e1b89d8a41971bc84fd"),
	PlaySound(sound=S0051_FIRE_THROW_BIG),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=12, destinations=["command_0x353706"]),
	Jmp(["extracted_subr_1b2d8b1adca04e1b89d8a41971bc84fd"]),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=14, destinations=["command_0x353706"]),
	Jmp(["extracted_subr_bf9c5dd6853546faa4f77e860d348331"]),
	Jmp(["command_0x351BFD"]),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	ReturnSubroutine(),
	SetOMEM60To072C(identifier="command_0x352523"),
	DisplayMessageAtOMEM60As(ATTACK_NAME),
	Jmp(["command_0x351899"]),
	ReturnSubroutine(),
	SetOMEM60To072C(identifier="command_0x35252B"),
	DisplayMessageAtOMEM60As(SPELL_NAME),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x6F, identifier="command_0x35252F"),
	SetAMEM8BitToConst(0x6F, 1, identifier="extracted_subr_5c5c6a8bf97145ca995fffe090aab8f4"),
	SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F, identifier="extracted_subr_5469bedb5b8f4e03a6422dab68227bc3"),
	RemoveObject(),
	ReturnObjectQueue(),
	ClearAMEM8Bit(0x6F, identifier="command_0x35253B"),
	Jmp(["extracted_subr_5c5c6a8bf97145ca995fffe090aab8f4"], identifier="extracted_subr_60794ae2994a4d3c99186ce19dc2c129"),
	ReturnObjectQueue(),
	Pause1Frame(identifier="command_0x352546"),
	SetAMEM8BitToOMEMMain(amem=0x68, omem=0x68),
	JmpIfAMEM8BitNotEqualsConst(0x68, 1, ["command_0x352546"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x352552"),
	SetAMEM8BitToAMEM(amem=0x68, source_amem=0x68, upper=0x60),
	JmpIfAMEM8BitNotEqualsConst(0x68, 1, ["command_0x352552"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x35255E"),
	SetAMEM8BitToAMEM(amem=0x67, source_amem=0x67, upper=0x60),
	JmpIfAMEM8BitNotEqualsConst(0x67, 1, ["command_0x35255E"]),
	ReturnSubroutine()
])
