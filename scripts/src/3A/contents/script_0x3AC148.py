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

script = AnimationScriptBlock(expected_size=168, expected_beginning=0x3AC148, script=[
	Jmp(["extracted_subr_17d8b8db851048448b6b21d67c380ec8"]),
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=236, y=46, z=0, set_x=True, set_y=True, set_z=True),
	NewSpriteAtCoords(sprite_id=SPR0331_BANDANA_BLUE, sequence=0, priority=2, vram_address=0x7A00, palette_row=12, overwrite_vram=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	SummonMonster(monster=BANDANABLUEEnemy, position=1, bit_7=True),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=216, y=56, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_834a0ab4b5c045ddb7557569d2c5861a"]),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=186, y=71, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_0305d828e85f429db983b186287ae625"]),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=136, y=96, z=0, set_x=True, set_y=True, set_z=True),
	Jmp(["extracted_subr_c7433a28b98f4068bb9231b4ffefcd1c"]),
	JmpIfAMEMBitsSet(0x67, [0], ["command_0x3AC1EA"]),
	Jmp(["extracted_subr_9aab148e27f648beaad50bb65bae45ec"]),
	Jmp(["extracted_subr_8864582f575a4292a8a916e420d38f61"]),
	Pause1Frame(identifier="command_0x3AC1EA"),
	SpriteSequence(sequence=0, looping_off=True, mirror=True),
	Jmp(["command_0x3AC1EA"])
])
