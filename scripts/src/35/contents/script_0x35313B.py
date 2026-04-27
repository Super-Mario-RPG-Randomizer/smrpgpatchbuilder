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
	SpriteSequence(sequence=3, identifier="command_0x35313B"),
	PauseScriptUntilSpriteSequenceDone(),
	Jmp(["extracted_subr_aa71dbfdb7214dc19edb1e8900087ba4"]),
	RunSubroutine(["command_0x352F2F"]),
	ResetSpriteSequence(),
	ReturnSubroutine(),
	Jmp(["command_0x351899"]),
	Jmp(["extracted_subr_bb437a7fa02b457da88143b578e987ed"]),
	Jmp(["extracted_subr_a97839a802c641eeb8a9b7bebd71e95b"]),
	SpriteSequence(sequence=1, identifier="command_0x35315A"),
	PauseScriptUntilSpriteSequenceDone(identifier="extracted_subr_eab774a4710a445db970f2a33619b8e6"),
	Jmp(["command_0x3505D5"]),
	SpriteSequence(sequence=2, identifier="command_0x353160"),
	Jmp(["extracted_subr_eab774a4710a445db970f2a33619b8e6"]),
	SpriteSequence(sequence=3, identifier="command_0x353166"),
	Jmp(["extracted_subr_eab774a4710a445db970f2a33619b8e6"]),
	SpriteSequence(sequence=4, identifier="command_0x35316C"),
	Jmp(["extracted_subr_eab774a4710a445db970f2a33619b8e6"]),
	SpriteSequence(sequence=5, identifier="command_0x353172"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20),
	PlaySound(sound=S0093_BOWYER_ARROW_LOCK_BUTTON),
	Jmp(["extracted_subr_eab774a4710a445db970f2a33619b8e6"]),
	Jmp(["command_0x351899"]),
	Jmp(["command_0x3508B5"], identifier="extracted_subr_449dfa590a0f4ff7ae00b5d3af4d0b30"),
	SpriteSequence(sequence=2, identifier="command_0x353185"),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=6, looping_off=True),
	Jmp(["command_0x3505D5"]),
	SpriteSequence(sequence=5, identifier="command_0x35318D"),
	Jmp(["extracted_subr_pos1_1a12b5182f13443eb308dfb7c4f4c0cc"]),
	SpriteSequence(sequence=6, identifier="command_0x353194"),
	Jmp(["extracted_subr_pos1_1a12b5182f13443eb308dfb7c4f4c0cc"]),
	SpriteSequence(sequence=7, identifier="command_0x35319B"),
	Jmp(["extracted_subr_pos1_1a12b5182f13443eb308dfb7c4f4c0cc"]),
	SpriteSequence(sequence=1, identifier="command_0x3531A2"),
	PauseScriptUntilSpriteSequenceDone(identifier="extracted_subr_079447f8e5f443a0b69d57718df7ec05"),
	Jmp(["extracted_subr_449dfa590a0f4ff7ae00b5d3af4d0b30"]),
	Jmp(["extracted_subr_079447f8e5f443a0b69d57718df7ec05"]),
	SpriteSequence(sequence=3, identifier="command_0x3531AE"),
	Jmp(["extracted_subr_079447f8e5f443a0b69d57718df7ec05"]),
	SpriteSequence(sequence=4, identifier="command_0x3531B4"),
	Jmp(["extracted_subr_079447f8e5f443a0b69d57718df7ec05"]),
	SpriteSequence(sequence=5, identifier="command_0x3531BA"),
	Jmp(["extracted_subr_079447f8e5f443a0b69d57718df7ec05"]),
	SpriteSequence(sequence=6, identifier="command_0x3531C0"),
	PauseScriptUntilSpriteSequenceDone(),
	SetAMEM8BitToConst(0x64, 200),
	SetRAMRelative7EToAMEM8Bit(0x7E001A, 0x64, identifier="extracted_subr_9615d17255d2488aa7535a286955efba"),
	Jmp(["command_0x3508B5"]),
	SpriteSequence(sequence=7, identifier="command_0x3531CE"),
	Jmp(["extracted_subr_079447f8e5f443a0b69d57718df7ec05"]),
	SpriteSequence(sequence=8, identifier="command_0x3531D4"),
	Jmp(["extracted_subr_079447f8e5f443a0b69d57718df7ec05"]),
	SpriteSequence(sequence=9, looping_on=True, identifier="command_0x3531DA"),
	Jmp(["command_0x3508B5"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0012_TOADSTOOL_FALLEN_CRYING, sequence=1, store_to_vram=True, store_palette=True, overlap_all_sprites=True, identifier="command_0x3531DF"),
	PauseScriptUntilSpriteSequenceDone(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0007_TOADSTOOL_WALKING_DOWN_LEFT, sequence=0, store_to_vram=True, store_palette=True, overlap_all_sprites=True),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
