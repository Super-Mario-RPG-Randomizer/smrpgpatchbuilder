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

script = AnimationScriptBlock(expected_size=179, expected_beginning=0x35313B, script=[
	Jmp(["command_0x352506"], identifier="command_0x35313B"),
	SpriteSequence(sequence=3, identifier="command_0x35313E"),
	PauseScriptUntilSpriteSequenceDone(identifier="command_0x353140"),
	RunSubroutine(["command_0x352F29"]),
	ResetSpriteSequence(),
	ReturnSubroutine(),
	Jmp(["command_0x35250E"], identifier="command_0x353146"),
	SpriteSequence(sequence=4, identifier="command_0x353149"),
	Jmp(["command_0x353140"]),
	Jmp(["command_0x3522D3"], identifier="command_0x35314E"),
	SpriteSequence(sequence=1, identifier="command_0x353151"),
	PauseScriptUntilSpriteSequenceDone(identifier="command_0x353153"),
	Jmp(["command_0x3505D5"]),
	SpriteSequence(sequence=2, identifier="command_0x353157"),
	Jmp(["command_0x353153"]),
	SpriteSequence(sequence=3, identifier="command_0x35315C"),
	Jmp(["command_0x353153"]),
	SpriteSequence(sequence=4, identifier="command_0x353161"),
	Jmp(["command_0x353153"]),
	SpriteSequence(sequence=5, identifier="command_0x353166"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20),
	PlaySound(sound=S0093_BOWYER_ARROW_LOCK_BUTTON),
	Jmp(["command_0x353153"]),
	SpriteSequence(sequence=4, identifier="command_0x353171"),
	PauseScriptUntilSpriteSequenceDone(identifier="command_0x353173"),
	Jmp(["command_0x350E29"]),
	SpriteSequence(sequence=2, identifier="command_0x353177"),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=6, looping_off=True),
	Jmp(["command_0x3505D5"]),
	SpriteSequence(sequence=5, identifier="command_0x35317F"),
	Jmp(["command_0x353173"]),
	SpriteSequence(sequence=6, identifier="command_0x353184"),
	Jmp(["command_0x353173"]),
	SpriteSequence(sequence=7, identifier="command_0x353189"),
	Jmp(["command_0x353173"]),
	SpriteSequence(sequence=1, identifier="command_0x35318E"),
	PauseScriptUntilSpriteSequenceDone(identifier="command_0x353190"),
	Jmp(["command_0x350D58"]),
	SpriteSequence(sequence=2, identifier="command_0x353194"),
	Jmp(["command_0x353190"]),
	SpriteSequence(sequence=3, identifier="command_0x353199"),
	Jmp(["command_0x353190"]),
	SpriteSequence(sequence=4, identifier="command_0x35319E"),
	Jmp(["command_0x353190"]),
	SpriteSequence(sequence=5, identifier="command_0x3531A3"),
	Jmp(["command_0x353190"]),
	SpriteSequence(sequence=6, identifier="command_0x3531A8"),
	PauseScriptUntilSpriteSequenceDone(),
	SetAMEM8BitToConst(0x64, 200),
	SetRAMRelative7EToAMEM8Bit(0x7E001A, 0x64, identifier="command_0x3531AF"),
	Jmp(["command_0x350D58"]),
	SpriteSequence(sequence=7, identifier="command_0x3531B6"),
	Jmp(["command_0x353190"]),
	SpriteSequence(sequence=8, identifier="command_0x3531BB"),
	Jmp(["command_0x353190"]),
	SpriteSequence(sequence=9, looping_on=True, identifier="command_0x3531C0"),
	Jmp(["command_0x350D58"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0012_TOADSTOOL_FALLEN_CRYING, sequence=1, store_to_vram=True, store_palette=True, overlap_all_sprites=True, identifier="command_0x3531C5"),
	PauseScriptUntilSpriteSequenceDone(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0007_TOADSTOOL_WALKING_DOWN_LEFT, sequence=0, store_to_vram=True, store_palette=True, overlap_all_sprites=True),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
