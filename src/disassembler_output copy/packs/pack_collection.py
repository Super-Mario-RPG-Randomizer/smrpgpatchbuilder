"""ROM's PackCollection disassembled from the original game."""

from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    Formation,
    FormationMember,
    FormationPack,
    PackCollection,
)
from smrpgpatchbuilder.datatypes.battles.music import (
    NormalBattleMusic,
    MidbossMusic,
    BossMusic,
    Smithy1Music,
    CorndillyMusic,
    BoosterHillMusic,
    VolcanoMusic,
    CulexMusic,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield
from ..enemies.enemies import *
from ..variables.pack_names import *
from ..variables.formation_names import *


# ============================================================================
# Formation Declarations
# ============================================================================

FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN = Formation(
    id=0,
    members=[
        FormationMember(TERRAPINEnemy, 167, 135),
    ],
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0001_FORM0001_FOUR_BOBOMB_HENCHMEN = Formation(
    id=1,
    members=[
        FormationMember(TERRAPINEnemy, 151, 111),
        FormationMember(TERRAPINEnemy, 183, 151),
    ],
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0002_FORM0002_APPRENTICE_HENCHMAN = Formation(
    id=2,
    members=[
        FormationMember(TERRAPINEnemy, 167, 111),
        FormationMember(TERRAPINEnemy, 151, 143),
        FormationMember(TERRAPINEnemy, 215, 135),
    ],
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0003_FORM0003 = Formation(
    id=3,
    members=[
        FormationMember(TERRAPINEnemy, 135, 119),
        FormationMember(TERRAPINEnemy, 167, 111),
        FormationMember(TERRAPINEnemy, 183, 143),
        FormationMember(TERRAPINEnemy, 215, 135),
    ],
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0004_FORM0004_TWO_SPIKEYS = Formation(
    id=4,
    members=[
        FormationMember(SPIKEYEnemy, 135, 127),
        FormationMember(SPIKEYEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0005_FORM0005_SPIKEY_AND_TROOPA = Formation(
    id=5,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SKYTROOPAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0006_FORM0006_TWO_SPIKEYS_FROG = Formation(
    id=6,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SPIKEYEnemy, 199, 151),
        FormationMember(FROGOGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0007_FORM0007_THREE_SPIKEYS = Formation(
    id=7,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SPIKEYEnemy, 199, 119),
        FormationMember(SPIKEYEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0008_FORM0008_ONE_TROOPA = Formation(
    id=8,
    members=[
        FormationMember(SKYTROOPAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0009_FORM0009_TWO_TROOPAS = Formation(
    id=9,
    members=[
        FormationMember(SKYTROOPAEnemy, 135, 119),
        FormationMember(SKYTROOPAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0010_FORM0010_TWO_TROOPAS_FROG = Formation(
    id=10,
    members=[
        FormationMember(SKYTROOPAEnemy, 199, 151),
        FormationMember(SKYTROOPAEnemy, 135, 119),
        FormationMember(FROGOGEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0011_FORM0011_TWO_TROOPAS_GOOMBA = Formation(
    id=11,
    members=[
        FormationMember(SKYTROOPAEnemy, 167, 103),
        FormationMember(SKYTROOPAEnemy, 231, 135),
        None,
        FormationMember(GOOMBAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0012_FORM0012_TWO_GOOMBAS = Formation(
    id=12,
    members=[
        FormationMember(GOOMBAEnemy, 135, 119),
        FormationMember(GOOMBAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0013_FORM0013_THREE_GOOMBAS = Formation(
    id=13,
    members=[
        FormationMember(GOOMBAEnemy, 167, 111),
        FormationMember(GOOMBAEnemy, 167, 135),
        FormationMember(GOOMBAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0014_FORM0014_TWO_GOOMBAS_SPIKEY = Formation(
    id=14,
    members=[
        FormationMember(GOOMBAEnemy, 167, 111),
        FormationMember(GOOMBAEnemy, 215, 135),
        FormationMember(SPIKEYEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0015_FORM0015_GOOMBA_FROG_SPIKEY = Formation(
    id=15,
    members=[
        FormationMember(GOOMBAEnemy, 167, 135),
        FormationMember(FROGOGEnemy, 167, 111),
        FormationMember(SPIKEYEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0016_FORM0016_ONE_K9 = Formation(
    id=16,
    members=[
        FormationMember(K9Enemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0017_FORM0017_TWO_K9 = Formation(
    id=17,
    members=[
        FormationMember(K9Enemy, 199, 159),
        FormationMember(K9Enemy, 151, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0018_FORM0018_TWO_K9_SPIKEY = Formation(
    id=18,
    members=[
        FormationMember(K9Enemy, 135, 119),
        FormationMember(K9Enemy, 199, 151),
        FormationMember(SPIKEYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0019_FORM0019_ONE_K9_TWO_FROG = Formation(
    id=19,
    members=[
        FormationMember(K9Enemy, 183, 127),
        FormationMember(FROGOGEnemy, 215, 143),
        FormationMember(FROGOGEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0021_FORM0021_TWO_SHYSTER = Formation(
    id=21,
    members=[
        FormationMember(SHYSTEREnemy, 167, 119),
        FormationMember(SHYSTEREnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0022_FORM0022_THREE_SHYSTER = Formation(
    id=22,
    members=[
        FormationMember(SHYSTEREnemy, 151, 111),
        FormationMember(SHYSTEREnemy, 215, 143),
        FormationMember(SHYSTEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0024_FORM0024_TWO_RATFUNKS = Formation(
    id=24,
    members=[
        FormationMember(RATFUNKEnemy, 199, 143),
        FormationMember(RATFUNKEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0025_FORM0025_TWO_RATFUNKS_ONE_SHADOW = Formation(
    id=25,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(SHADOWEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0026_FORM0026_TWO_RATFUNKS_ONE_HOBGOBLIN = Formation(
    id=26,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(HOBGOBLINEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0027_FORM0027_ONE_RATFUNK_TWO_HOBGOBLINS = Formation(
    id=27,
    members=[
        FormationMember(RATFUNKEnemy, 167, 135),
        None,
        FormationMember(HOBGOBLINEnemy, 167, 103),
        FormationMember(HOBGOBLINEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0029_FORM0029_ONE_BIGBOO_ONE_SHADOW = Formation(
    id=29,
    members=[
        FormationMember(THEBIGBOOEnemy, 151, 119),
        FormationMember(SHADOWEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0030_FORM0030_BIGBOO_SHADOW_HOBGOBLIN = Formation(
    id=30,
    members=[
        FormationMember(THEBIGBOOEnemy, 119, 119),
        FormationMember(SHADOWEnemy, 167, 135),
        FormationMember(HOBGOBLINEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0031_FORM0031_THREE_BIGBOO_ONE_SHADOW = Formation(
    id=31,
    members=[
        FormationMember(THEBIGBOOEnemy, 231, 135),
        FormationMember(THEBIGBOOEnemy, 151, 143),
        FormationMember(THEBIGBOOEnemy, 167, 103),
        FormationMember(SHADOWEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0033_FORM0034_THREE_GOBYS = Formation(
    id=33,
    members=[
        FormationMember(GOBYEnemy, 135, 119),
        FormationMember(GOBYEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0034_FORM0036_TWO_CROOKS = Formation(
    id=34,
    members=[
        FormationMember(GOBYEnemy, 151, 119),
        FormationMember(GOBYEnemy, 215, 119),
        FormationMember(GOBYEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0036_FORM0038_ONE_CROOK_TWO_SNAPDRAGONS = Formation(
    id=36,
    members=[
        FormationMember(CROOKEnemy, 167, 111),
        FormationMember(CROOKEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0037_FORM0039_CROOK_STARSLAP_ARACHNE = Formation(
    id=37,
    members=[
        FormationMember(CROOKEnemy, 199, 143),
        FormationMember(CROOKEnemy, 151, 119),
        FormationMember(SHYGUYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0038_FORM0040_ONE_SHYGUY_HENCHMAN = Formation(
    id=38,
    members=[
        FormationMember(CROOKEnemy, 183, 127),
        FormationMember(SNAPDRAGONEnemy, 151, 111),
        FormationMember(SNAPDRAGONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0039_FORM0041_ONE_SHYGUY_ONE_STARSLAP = Formation(
    id=39,
    members=[
        FormationMember(CROOKEnemy, 199, 159),
        None,
        None,
        FormationMember(STARSLAPEnemy, 215, 127),
        FormationMember(ARACHNEEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0041_FORM0043_SHYGUY_CROOK_ARACHNE = Formation(
    id=41,
    members=[
        FormationMember(SHYGUYEnemy, 151, 111),
        None,
        FormationMember(STARSLAPEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0042_FORM0044_STARSLAP_SHYGUY = Formation(
    id=42,
    members=[
        FormationMember(SHYGUYEnemy, 135, 103),
        FormationMember(SHYGUYEnemy, 215, 143),
        None,
        FormationMember(SNAPDRAGONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0043_FORM0045_STARSLAP_ARACHNE = Formation(
    id=43,
    members=[
        FormationMember(SHYGUYEnemy, 231, 135),
        None,
        FormationMember(CROOKEnemy, 199, 143),
        FormationMember(ARACHNEEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0044_FORM0046_STARSLAP_TWO_SNAPDRAGONS = Formation(
    id=44,
    members=[
        FormationMember(STARSLAPEnemy, 199, 159),
        FormationMember(SHYGUYEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0045_FORM0047_FOUR_STARSLAPS = Formation(
    id=45,
    members=[
        FormationMember(STARSLAPEnemy, 215, 151),
        FormationMember(ARACHNEEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0046_FORM0048_ONE_WIGGLER = Formation(
    id=46,
    members=[
        FormationMember(STARSLAPEnemy, 167, 135),
        FormationMember(SNAPDRAGONEnemy, 151, 111),
        FormationMember(SNAPDRAGONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0047_FORM0049_ONE_WIGGLER_ONE_AMANITA = Formation(
    id=47,
    members=[
        FormationMember(STARSLAPEnemy, 199, 151),
        FormationMember(STARSLAPEnemy, 167, 103),
        FormationMember(STARSLAPEnemy, 231, 135),
        FormationMember(STARSLAPEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0048_FORM0050_TWO_WIGGLERS = Formation(
    id=48,
    members=[
        FormationMember(WIGGLEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0049_FORM0051_ONE_WIGGLER_ONE_GUERRILLA = Formation(
    id=49,
    members=[
        FormationMember(WIGGLEREnemy, 151, 111),
        FormationMember(AMANITAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0050_FORM0052_TWO_AMANITAS = Formation(
    id=50,
    members=[
        FormationMember(WIGGLEREnemy, 151, 111),
        FormationMember(WIGGLEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0051_FORM0053_TWO_AMANITAS_ONE_BUZZER = Formation(
    id=51,
    members=[
        FormationMember(WIGGLEREnemy, 151, 119),
        None,
        FormationMember(GUERRILLAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0052_FORM0054_TWO_AMANITAS_ONE_OCTOLOT = Formation(
    id=52,
    members=[
        FormationMember(AMANITAEnemy, 135, 127),
        FormationMember(AMANITAEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0053_FORM0055_AMANITA_BUZZER_GUERRILLA = Formation(
    id=53,
    members=[
        FormationMember(AMANITAEnemy, 199, 151),
        FormationMember(AMANITAEnemy, 135, 119),
        FormationMember(BUZZEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0054_FORM0056_BUZZER_OCTOLOT = Formation(
    id=54,
    members=[
        FormationMember(AMANITAEnemy, 199, 151),
        FormationMember(AMANITAEnemy, 135, 119),
        FormationMember(OCTOLOTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0055_FORM0057_TWO_BUZZERS_ONE_AMANITA = Formation(
    id=55,
    members=[
        FormationMember(AMANITAEnemy, 151, 127),
        None,
        FormationMember(GUERRILLAEnemy, 215, 143),
        FormationMember(BUZZEREnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0056_FORM0058_BUZZER_GUERRILLA = Formation(
    id=56,
    members=[
        FormationMember(BUZZEREnemy, 135, 119),
        FormationMember(OCTOLOTEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0057_FORM0059_BUZZER_GUERRILLA_2 = Formation(
    id=57,
    members=[
        FormationMember(BUZZEREnemy, 167, 103),
        FormationMember(BUZZEREnemy, 231, 135),
        FormationMember(AMANITAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0058_FORM0060_ONE_SPARKY = Formation(
    id=58,
    members=[
        FormationMember(BUZZEREnemy, 199, 151),
        None,
        FormationMember(GUERRILLAEnemy, 151, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0059_FORM0061_TWO_SPARKY_ONE_SHYRANGER = Formation(
    id=59,
    members=[
        FormationMember(BUZZEREnemy, 199, 159),
        None,
        FormationMember(GUERRILLAEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0060_FORM0062_THREE_SPARKY = Formation(
    id=60,
    members=[
        FormationMember(SPARKYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0061_FORM0063 = Formation(
    id=61,
    members=[
        FormationMember(SPARKYEnemy, 167, 111),
        FormationMember(SPARKYEnemy, 215, 135),
        FormationMember(SHYRANGEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0062_FORM0064 = Formation(
    id=62,
    members=[
        FormationMember(SPARKYEnemy, 167, 135),
        FormationMember(SPARKYEnemy, 151, 111),
        FormationMember(SPARKYEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0064_FORM0066 = Formation(
    id=64,
    members=[
        FormationMember(GOOMBAEnemy, 183, 127),
        FormationMember(SHYRANGEREnemy, 135, 119),
        FormationMember(SHYRANGEREnemy, 167, 103),
        FormationMember(SHYRANGEREnemy, 199, 151),
        FormationMember(SHYRANGEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0065_FORM0067 = Formation(
    id=65,
    members=[
        FormationMember(GOOMBAEnemy, 199, 151),
        FormationMember(GOOMBAEnemy, 135, 119),
        FormationMember(SHYRANGEREnemy, 183, 111),
        FormationMember(SHYRANGEREnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0066_FORM0068_ONE_PIRANHA = Formation(
    id=66,
    members=[
        FormationMember(GOOMBAEnemy, 135, 119),
        FormationMember(GOOMBAEnemy, 199, 151),
        FormationMember(PIRANHAPLANTEnemy, 199, 119),
        FormationMember(PIRANHAPLANTEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0067_FORM0069_TWO_PIRANHA_ONE_SHYRANGER = Formation(
    id=67,
    members=[
        FormationMember(GOOMBAEnemy, 167, 135),
        None,
        FormationMember(PIRANHAPLANTEnemy, 231, 151),
        FormationMember(PIRANHAPLANTEnemy, 135, 103),
        FormationMember(SPARKYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0068_FORM0070_THREE_PIRANHA = Formation(
    id=68,
    members=[
        FormationMember(PIRANHAPLANTEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0069_FORM0071_FIVE_PIRANHA = Formation(
    id=69,
    members=[
        FormationMember(PIRANHAPLANTEnemy, 215, 143),
        FormationMember(PIRANHAPLANTEnemy, 151, 111),
        FormationMember(SHYRANGEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0070_FORM0072_ONE_BOBOMB = Formation(
    id=70,
    members=[
        FormationMember(PIRANHAPLANTEnemy, 167, 111),
        FormationMember(PIRANHAPLANTEnemy, 167, 135),
        FormationMember(PIRANHAPLANTEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0071_FORM0073_TWO_BOBOMB_ONE_CLUSTER = Formation(
    id=71,
    members=[
        FormationMember(PIRANHAPLANTEnemy, 151, 143),
        FormationMember(PIRANHAPLANTEnemy, 151, 111),
        FormationMember(PIRANHAPLANTEnemy, 199, 119),
        FormationMember(PIRANHAPLANTEnemy, 231, 143),
        FormationMember(PIRANHAPLANTEnemy, 199, 159),
    ],
    music=NormalBattleMusic(),
)

FORM0072_FORM0074_FOUR_BOBOMB = Formation(
    id=72,
    members=[
        FormationMember(BOBOMBEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0073_FORM0075_TWO_BOBOMB_ENIGMA_CLUSTER = Formation(
    id=73,
    members=[
        FormationMember(BOBOMBEnemy, 135, 119),
        FormationMember(BOBOMBEnemy, 199, 151),
        FormationMember(CLUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0074_FORM0076_SPARKY_ENIGMA = Formation(
    id=74,
    members=[
        FormationMember(BOBOMBEnemy, 151, 127),
        FormationMember(BOBOMBEnemy, 167, 103),
        FormationMember(BOBOMBEnemy, 199, 151),
        FormationMember(BOBOMBEnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0075_FORM0077_TWO_SPARKY_ONE_BOBOMB = Formation(
    id=75,
    members=[
        FormationMember(BOBOMBEnemy, 135, 119),
        FormationMember(BOBOMBEnemy, 199, 151),
        FormationMember(ENIGMAEnemy, 183, 111),
        FormationMember(CLUSTEREnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0076_FORM0078_ONE_SPARKY_TWO_CLUSTER = Formation(
    id=76,
    members=[
        FormationMember(SPARKYEnemy, 199, 151),
        FormationMember(ENIGMAEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0077_FORM0079_TWO_SPARKY_TWO_ENIGMA = Formation(
    id=77,
    members=[
        FormationMember(SPARKYEnemy, 167, 111),
        FormationMember(SPARKYEnemy, 215, 135),
        FormationMember(BOBOMBEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0078_FORM0080_TWO_MAGMITE = Formation(
    id=78,
    members=[
        FormationMember(SPARKYEnemy, 183, 127),
        FormationMember(CLUSTEREnemy, 231, 143),
        FormationMember(CLUSTEREnemy, 151, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0079_FORM0081_MAGMITE_BOBOMB_SPARKY = Formation(
    id=79,
    members=[
        FormationMember(SPARKYEnemy, 183, 143),
        FormationMember(SPARKYEnemy, 151, 127),
        FormationMember(ENIGMAEnemy, 167, 103),
        FormationMember(ENIGMAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0080_FORM0082_TWO_MAGMITE_TWO_CLUSTER = Formation(
    id=80,
    members=[
        FormationMember(MAGMITEEnemy, 167, 111),
        FormationMember(MAGMITEEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0081_FORM0083_TWO_MAGMITE_BOBOMB_CLUSTER = Formation(
    id=81,
    members=[
        FormationMember(MAGMITEEnemy, 151, 111),
        FormationMember(BOBOMBEnemy, 183, 127),
        FormationMember(SPARKYEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0082_FORM0084_ONE_LAKITU = Formation(
    id=82,
    members=[
        FormationMember(MAGMITEEnemy, 151, 127),
        FormationMember(MAGMITEEnemy, 183, 143),
        FormationMember(CLUSTEREnemy, 167, 103),
        FormationMember(CLUSTEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0083_FORM0085_LAKITU_SPIKESTER_ARTICHOKER = Formation(
    id=83,
    members=[
        FormationMember(MAGMITEEnemy, 135, 103),
        FormationMember(MAGMITEEnemy, 231, 151),
        FormationMember(BOBOMBEnemy, 167, 135),
        None,
        FormationMember(CLUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0084_FORM0086_THREE_LAKITU = Formation(
    id=84,
    members=[
        FormationMember(LAKITUEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0085_FORM0087_TWO_LAKITU_ONE_ARTICHOKER = Formation(
    id=85,
    members=[
        FormationMember(LAKITUEnemy, 135, 119),
        FormationMember(SPIKESTEREnemy, 199, 159),
        FormationMember(ARTICHOKEREnemy, 183, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0086_FORM0088_SPIKESTER_CARROBOSCIS = Formation(
    id=86,
    members=[
        FormationMember(LAKITUEnemy, 151, 111),
        FormationMember(LAKITUEnemy, 183, 127),
        FormationMember(LAKITUEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0087_FORM0089_TWO_SPIKESTER_ONE_ARTICHOKER = Formation(
    id=87,
    members=[
        FormationMember(LAKITUEnemy, 231, 151),
        FormationMember(LAKITUEnemy, 135, 103),
        None,
        FormationMember(ARTICHOKEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0088_FORM0090_ONE_SPIKESTER_TWO_CARROBOSCIS = Formation(
    id=88,
    members=[
        FormationMember(SPIKESTEREnemy, 215, 143),
        FormationMember(CARROBOSCISEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0089_FORM0091_FOUR_SPIKESTER_ONE_CARROBOSCIS = Formation(
    id=89,
    members=[
        FormationMember(SPIKESTEREnemy, 199, 151),
        FormationMember(SPIKESTEREnemy, 135, 119),
        FormationMember(ARTICHOKEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0090_FORM0092_SPOOKUM_ORBUSER = Formation(
    id=90,
    members=[
        FormationMember(SPIKESTEREnemy, 183, 127),
        FormationMember(CARROBOSCISEnemy, 135, 119),
        FormationMember(CARROBOSCISEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0091_FORM0093_TWO_SPOOKUM_ONE_JESTER = Formation(
    id=91,
    members=[
        FormationMember(SPIKESTEREnemy, 119, 111),
        FormationMember(SPIKESTEREnemy, 215, 159),
        FormationMember(SPIKESTEREnemy, 215, 135),
        FormationMember(SPIKESTEREnemy, 167, 111),
        FormationMember(CARROBOSCISEnemy, 151, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0092_FORM0094_SPOOKUM_REMOCON_ORBUSER = Formation(
    id=92,
    members=[
        FormationMember(SPOOKUMEnemy, 199, 135),
        FormationMember(ORBUSEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0093_FORM0095_TWO_SPOOKUM_ONE_REMOCON = Formation(
    id=93,
    members=[
        FormationMember(SPOOKUMEnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 151),
        FormationMember(JESTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0094_FORM0096_ONE_ROBOMB = Formation(
    id=94,
    members=[
        FormationMember(SPOOKUMEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 167, 151),
        FormationMember(ORBUSEREnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0095_FORM0097_THREE_ROBOMB = Formation(
    id=95,
    members=[
        FormationMember(SPOOKUMEnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 151),
        FormationMember(REMOCONEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0096_FORM0098_TWO_ROBOMB_ONE_REMOCON = Formation(
    id=96,
    members=[
        FormationMember(ROBOMBEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0097_FORM0099_FOUR_ROBOMB_ONE_ORBUSER = Formation(
    id=97,
    members=[
        FormationMember(ROBOMBEnemy, 183, 127),
        FormationMember(ROBOMBEnemy, 199, 119),
        FormationMember(ROBOMBEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0098_FORM0100_CHOMP_JESTER = Formation(
    id=98,
    members=[
        FormationMember(ROBOMBEnemy, 215, 143),
        FormationMember(ROBOMBEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0099_FORM0101_CHOMP_ROBOMB_REMOCON = Formation(
    id=99,
    members=[
        FormationMember(ROBOMBEnemy, 135, 127),
        FormationMember(ROBOMBEnemy, 231, 127),
        FormationMember(ROBOMBEnemy, 183, 103),
        FormationMember(ROBOMBEnemy, 183, 151),
        FormationMember(ORBUSEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0100_FORM0102_TWO_CHOMP_ONE_ORBUSER = Formation(
    id=100,
    members=[
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(JESTEREnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0101_FORM0103_ONE_CHOMP_TWO_JESTER = Formation(
    id=101,
    members=[
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(ROBOMBEnemy, 151, 135),
        FormationMember(REMOCONEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0102_FORM0104_BLASTER_SPOOKUM = Formation(
    id=102,
    members=[
        FormationMember(CHOMPEnemy, 151, 111),
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(ORBUSEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0103_FORM0105_BLASTER_SPOOKUM_REMOCON = Formation(
    id=103,
    members=[
        FormationMember(CHOMPEnemy, 199, 119),
        None,
        FormationMember(JESTEREnemy, 135, 103),
        FormationMember(JESTEREnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0104_FORM0106_TWO_BLASTER_ONE_SPOOKUM = Formation(
    id=104,
    members=[
        FormationMember(BLASTEREnemy, 167, 135),
        FormationMember(SPOOKUMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0105_FORM0107_BLASTER_TWO_ROBOMB_TWO_SPOOKUM = Formation(
    id=105,
    members=[
        FormationMember(BLASTEREnemy, 167, 135),
        FormationMember(SPOOKUMEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0106_FORM0108_ONE_TORTE = Formation(
    id=106,
    members=[
        FormationMember(BLASTEREnemy, 199, 151),
        FormationMember(BLASTEREnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0107_FORM0109_TWO_TORTE = Formation(
    id=107,
    members=[
        FormationMember(BLASTEREnemy, 199, 119),
        FormationMember(ROBOMBEnemy, 135, 103),
        FormationMember(ROBOMBEnemy, 231, 151),
        FormationMember(SPOOKUMEnemy, 151, 127),
        FormationMember(SPOOKUMEnemy, 183, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0108_FORM0110_THREE_TORTE = Formation(
    id=108,
    members=[
        FormationMember(TORTEEnemy2, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0109_FORM0111_FOUR_TORTE = Formation(
    id=109,
    members=[
        FormationMember(TORTEEnemy2, 215, 143),
        FormationMember(TORTEEnemy2, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0110_FORM0112_ONE_MUKU = Formation(
    id=110,
    members=[
        FormationMember(TORTEEnemy2, 183, 103),
        FormationMember(TORTEEnemy2, 151, 135),
        FormationMember(TORTEEnemy2, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0111_FORM0113_TWO_MUKU = Formation(
    id=111,
    members=[
        FormationMember(TORTEEnemy2, 167, 135),
        FormationMember(TORTEEnemy2, 199, 119),
        FormationMember(TORTEEnemy2, 151, 111),
        FormationMember(TORTEEnemy2, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0112_FORM0114_TWO_MUKU_ONE_PULSAR = Formation(
    id=112,
    members=[
        FormationMember(MUKUMUKUEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0113_FORM0115_MUKU_PULSAR_GECKO = Formation(
    id=113,
    members=[
        FormationMember(MUKUMUKUEnemy, 151, 119),
        FormationMember(MUKUMUKUEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0114_FORM0116_TWO_SACKIT = Formation(
    id=114,
    members=[
        FormationMember(MUKUMUKUEnemy, 151, 111),
        FormationMember(MUKUMUKUEnemy, 215, 143),
        FormationMember(PULSAREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0115_FORM0117_TWO_SACKIT_MUKU_GECKO = Formation(
    id=115,
    members=[
        FormationMember(MUKUMUKUEnemy, 183, 143),
        FormationMember(PULSAREnemy, 151, 111),
        FormationMember(GECKOEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0116_FORM0118_ONE_SACKIT_TWO_PULSAR = Formation(
    id=116,
    members=[
        FormationMember(SACKITEnemy, 199, 151),
        FormationMember(SACKITEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0117_FORM0119_SACKIT_MASTADOOM = Formation(
    id=117,
    members=[
        FormationMember(SACKITEnemy, 151, 127),
        FormationMember(SACKITEnemy, 183, 143),
        FormationMember(MUKUMUKUEnemy, 167, 103),
        FormationMember(GECKOEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0118_FORM0120_GECKO_SACKIT = Formation(
    id=118,
    members=[
        FormationMember(SACKITEnemy, 167, 135),
        None,
        None,
        FormationMember(PULSAREnemy, 167, 103),
        FormationMember(PULSAREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0119_FORM0121_GECKO_MASTADOOM = Formation(
    id=119,
    members=[
        FormationMember(SACKITEnemy, 215, 143),
        FormationMember(MASTADOOMEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0120_FORM0122_TWO_GECKO_TWO_MUKU_TWO_SACKIT = Formation(
    id=120,
    members=[
        FormationMember(GECKOEnemy, 151, 119),
        FormationMember(SACKITEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0121_FORM0123_TWO_GECKO_ONE_MASTADOOM = Formation(
    id=121,
    members=[
        FormationMember(GECKOEnemy, 151, 119),
        FormationMember(MASTADOOMEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0122_FORM0124_TWO_ZEOSTAR = Formation(
    id=122,
    members=[
        FormationMember(GECKOEnemy, 183, 143),
        FormationMember(GECKOEnemy, 151, 127),
        FormationMember(MUKUMUKUEnemy, 135, 103),
        FormationMember(MUKUMUKUEnemy, 231, 151),
        FormationMember(SACKITEnemy, 183, 111),
        FormationMember(SACKITEnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0123_FORM0125_TWO_ZEOSTAR_ONE_BLOOBER = Formation(
    id=123,
    members=[
        FormationMember(GECKOEnemy, 135, 103),
        FormationMember(GECKOEnemy, 231, 151),
        FormationMember(MASTADOOMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0124_FORM0126_TWO_ZEOSTAR_TWO_LEUKO = Formation(
    id=124,
    members=[
        FormationMember(ZEOSTAREnemy, 135, 119),
        FormationMember(ZEOSTAREnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0125_FORM0127_ZEOSTAR_LEUKO_CRUSTY = Formation(
    id=125,
    members=[
        FormationMember(ZEOSTAREnemy, 151, 135),
        FormationMember(ZEOSTAREnemy, 183, 103),
        FormationMember(BLOOBEREnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0126_FORM0128_BLOOPER_KIPPER = Formation(
    id=126,
    members=[
        FormationMember(ZEOSTAREnemy, 199, 119),
        FormationMember(ZEOSTAREnemy, 167, 135),
        FormationMember(LEUKOEnemy, 167, 103),
        FormationMember(LEUKOEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0127_FORM0129_THREE_BLOOBER = Formation(
    id=127,
    members=[
        FormationMember(ZEOSTAREnemy, 183, 127),
        FormationMember(LEUKOEnemy, 215, 143),
        FormationMember(CRUSTYEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0128_FORM0130_TWO_BLOOBER_KIPPER_CRUSTY = Formation(
    id=128,
    members=[
        FormationMember(BLOOBEREnemy, 151, 111),
        FormationMember(MRKIPPEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0129_FORM0131_TWO_BLOOBER_TWO_ZEOSTAR_ONE_LEUKO = Formation(
    id=129,
    members=[
        FormationMember(BLOOBEREnemy, 183, 127),
        FormationMember(BLOOBEREnemy, 231, 143),
        FormationMember(BLOOBEREnemy, 135, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0130_FORM0132_THREE_KIPPER = Formation(
    id=130,
    members=[
        FormationMember(BLOOBEREnemy, 151, 111),
        FormationMember(BLOOBEREnemy, 231, 151),
        FormationMember(MRKIPPEREnemy, 151, 143),
        FormationMember(CRUSTYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0131_FORM0133_TWO_KIPPER_ONE_CRUSTY = Formation(
    id=131,
    members=[
        FormationMember(BLOOBEREnemy, 231, 135),
        FormationMember(BLOOBEREnemy, 167, 103),
        FormationMember(ZEOSTAREnemy, 135, 127),
        FormationMember(ZEOSTAREnemy, 183, 151),
        FormationMember(LEUKOEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0132_FORM0134_TWO_KIPPER_ONE_CRUSTY_2 = Formation(
    id=132,
    members=[
        FormationMember(MRKIPPEREnemy, 151, 103),
        FormationMember(MRKIPPEREnemy, 215, 151),
        FormationMember(MRKIPPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0133_FORM0135_FOUR_KIPPER = Formation(
    id=133,
    members=[
        FormationMember(MRKIPPEREnemy, 199, 151),
        FormationMember(MRKIPPEREnemy, 135, 119),
        FormationMember(CRUSTYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0134_FORM0136_FOUR_BANDANA_RED = Formation(
    id=134,
    members=[
        FormationMember(MRKIPPEREnemy, 135, 119),
        FormationMember(MRKIPPEREnemy, 231, 135),
        FormationMember(CRUSTYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0135_FORM0137_FIVE_BANDANA_RED = Formation(
    id=135,
    members=[
        FormationMember(MRKIPPEREnemy, 215, 127),
        FormationMember(MRKIPPEREnemy, 199, 151),
        FormationMember(MRKIPPEREnemy, 167, 103),
        FormationMember(MRKIPPEREnemy, 151, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0136_FORM0138 = Formation(
    id=136,
    members=[
        FormationMember(BANDANAREDEnemy, 151, 127),
        FormationMember(BANDANAREDEnemy, 183, 143),
        FormationMember(BANDANAREDEnemy, 167, 103),
        FormationMember(BANDANAREDEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0137_FORM0139 = Formation(
    id=137,
    members=[
        FormationMember(BANDANAREDEnemy, 199, 151),
        FormationMember(BANDANAREDEnemy, 135, 119),
        FormationMember(BANDANAREDEnemy, 215, 127),
        FormationMember(BANDANAREDEnemy, 167, 135),
        FormationMember(BANDANAREDEnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0140_FORM0142_FOUR_BANDANABLUE = Formation(
    id=140,
    members=[
        FormationMember(BANDANABLUEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0141_FORM0143_FIVE_BANDANARED_HENCHMEN = Formation(
    id=141,
    members=[
        FormationMember(BANDANABLUEEnemy, 135, 119),
        FormationMember(BANDANABLUEEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0142_FORM0144_TWO_DRYBONES = Formation(
    id=142,
    members=[
        FormationMember(BANDANABLUEEnemy, 135, 127),
        FormationMember(BANDANABLUEEnemy, 167, 111),
        FormationMember(BANDANABLUEEnemy, 183, 151),
        FormationMember(BANDANABLUEEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0143_FORM0145_TWO_DRYBONES_ONE_GREAPER = Formation(
    id=143,
    members=[
        FormationMember(BANDANABLUEEnemy, 135, 119),
        FormationMember(BANDANABLUEEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 167, 103),
        FormationMember(GREAPEREnemy, 231, 135),
        FormationMember(STRAWHEADEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0144_FORM0146_DRYBONES_GREAPER_REACHER = Formation(
    id=144,
    members=[
        FormationMember(DRYBONESEnemy, 199, 151),
        FormationMember(DRYBONESEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0145_FORM0147_TWO_DRYBONES_TWO_GREAPER_ONE_REACHER = Formation(
    id=145,
    members=[
        FormationMember(DRYBONESEnemy, 135, 119),
        FormationMember(DRYBONESEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0146_FORM0148_ALLEYRAT_GORGON = Formation(
    id=146,
    members=[
        FormationMember(DRYBONESEnemy, 135, 119),
        FormationMember(GREAPEREnemy, 199, 151),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0147_FORM0149_TWO_ALLEYRAT_TWO_GREAPER = Formation(
    id=147,
    members=[
        FormationMember(DRYBONESEnemy, 167, 103),
        FormationMember(DRYBONESEnemy, 231, 135),
        FormationMember(GREAPEREnemy, 151, 127),
        FormationMember(GREAPEREnemy, 183, 143),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0148_FORM0150_TWO_ALLEYRAT_TWO_GORGON = Formation(
    id=148,
    members=[
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GORGONEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0149_FORM0151_ALLEYRAT_REACHER_GORGON = Formation(
    id=149,
    members=[
        FormationMember(ALLEYRATEnemy, 135, 119),
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 215, 127),
        FormationMember(GREAPEREnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0150_FORM0152_ONE_GREAPER = Formation(
    id=150,
    members=[
        FormationMember(ALLEYRATEnemy, 151, 127),
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GORGONEnemy, 183, 111),
        FormationMember(GORGONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0151_FORM0153_TWO_GREAPER_ONE_REACHER = Formation(
    id=151,
    members=[
        FormationMember(ALLEYRATEnemy, 231, 135),
        FormationMember(REACHEREnemy, 167, 135),
        FormationMember(GORGONEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0152_FORM0154_GREAPER_STRAWHEAD_REACHER = Formation(
    id=152,
    members=[
        FormationMember(GREAPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0153_FORM0155_GREAPER_GORGON_TWO_STRAWHEAD = Formation(
    id=153,
    members=[
        FormationMember(GREAPEREnemy, 151, 119),
        FormationMember(GREAPEREnemy, 199, 143),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0154_FORM0156_ONE_DRILLBIT = Formation(
    id=154,
    members=[
        FormationMember(GREAPEREnemy, 167, 135),
        FormationMember(STRAWHEADEnemy, 215, 135),
        FormationMember(REACHEREnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0155_FORM0157_TWO_DRILLBIT = Formation(
    id=155,
    members=[
        FormationMember(GREAPEREnemy, 167, 135),
        FormationMember(GORGONEnemy, 199, 119),
        FormationMember(STRAWHEADEnemy, 215, 143),
        FormationMember(STRAWHEADEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0156_FORM0158_THREE_DRILLBIT = Formation(
    id=156,
    members=[
        FormationMember(MARIOCLONESEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0157_FORM0159_FIVE_DRILLBIT = Formation(
    id=157,
    members=[
        FormationMember(MARIOCLONESEnemy, 167, 135),
        FormationMember(MARIOCLONESEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0158_FORM0160_STINGER_FINKFLOWER = Formation(
    id=158,
    members=[
        FormationMember(MARIOCLONESEnemy, 151, 119),
        FormationMember(MARIOCLONESEnemy, 183, 151),
        FormationMember(MARIOCLONESEnemy, 215, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0159_FORM0161_TWO_STINGER_ONE_OCTOVADER = Formation(
    id=159,
    members=[
        FormationMember(MARIOCLONESEnemy, 167, 119),
        FormationMember(MARIOCLONESEnemy, 199, 151),
        FormationMember(MARIOCLONESEnemy, 135, 119),
        FormationMember(MARIOCLONESEnemy, 199, 119),
        FormationMember(MARIOCLONESEnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0160_FORM0162_ONE_STINGER_TWO_FINKFLOWER = Formation(
    id=160,
    members=[
        FormationMember(STINGEREnemy, 151, 111),
        FormationMember(FINKFLOWEREnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0161_FORM0163_FOUR_STINGER = Formation(
    id=161,
    members=[
        FormationMember(STINGEREnemy, 135, 111),
        FormationMember(STINGEREnemy, 215, 151),
        FormationMember(OCTOVADEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0162_FORM0164_CHOW_OCTOVADER = Formation(
    id=162,
    members=[
        FormationMember(STINGEREnemy, 199, 119),
        None,
        FormationMember(FINKFLOWEREnemy, 215, 143),
        FormationMember(FINKFLOWEREnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0163_FORM0165_CHOW_SHOGUN = Formation(
    id=163,
    members=[
        FormationMember(STINGEREnemy, 183, 111),
        FormationMember(STINGEREnemy, 199, 151),
        FormationMember(STINGEREnemy, 215, 127),
        FormationMember(STINGEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0164_FORM0166_CHOW_SHOGUN_OCTOVADER = Formation(
    id=164,
    members=[
        FormationMember(CHOWEnemy, 135, 119),
        FormationMember(OCTOVADEREnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0165_FORM0167_CHOW_FINKFLOWER_TWO_SHOGUN = Formation(
    id=165,
    members=[
        FormationMember(CHOWEnemy, 151, 111),
        FormationMember(SHOGUNEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0166_FORM0168_ONE_CHOMPCHOMP = Formation(
    id=166,
    members=[
        FormationMember(CHOWEnemy, 199, 151),
        FormationMember(SHOGUNEnemy, 135, 119),
        FormationMember(OCTOVADEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0167_FORM0169_TWO_CHOMPCHOMP = Formation(
    id=167,
    members=[
        FormationMember(CHOWEnemy, 167, 135),
        FormationMember(FINKFLOWEREnemy, 199, 119),
        FormationMember(SHOGUNEnemy, 135, 119),
        FormationMember(SHOGUNEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0168_FORM0170_THREE_CHOMPCHOMP = Formation(
    id=168,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0169_FORM0171_FOUR_CHOMPCHOMP = Formation(
    id=169,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 151, 111),
        FormationMember(CHOMPCHOMPEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0170_FORM0172_ONE_SHYAWAY = Formation(
    id=170,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 151, 111),
        FormationMember(CHOMPCHOMPEnemy, 199, 119),
        FormationMember(CHOMPCHOMPEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0171_FORM0173_TWO_SHYAWAY_ONE_KRIFFID = Formation(
    id=171,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 135, 119),
        FormationMember(CHOMPCHOMPEnemy, 183, 111),
        FormationMember(CHOMPCHOMPEnemy, 215, 127),
        FormationMember(CHOMPCHOMPEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0172_FORM0174_TWO_SHYAWAY_ONE_RIBBITE = Formation(
    id=172,
    members=[
        FormationMember(SHYAWAYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0173_FORM0175_SHYAWAY_GECKIT_RIBBITE = Formation(
    id=173,
    members=[
        FormationMember(SHYAWAYEnemy, 151, 111),
        FormationMember(SHYAWAYEnemy, 215, 143),
        FormationMember(KRIFFIDEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0174_FORM0176_TWO_CHEWY = Formation(
    id=174,
    members=[
        FormationMember(SHYAWAYEnemy, 167, 103),
        FormationMember(SHYAWAYEnemy, 231, 135),
        FormationMember(RIBBITEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0175_FORM0177_TWO_CHEWY_ONE_SHYAWAY = Formation(
    id=175,
    members=[
        FormationMember(SHYAWAYEnemy, 215, 135),
        None,
        FormationMember(GECKITEnemy, 167, 143),
        None,
        FormationMember(RIBBITEEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0176_FORM0178_CHEWY_SPINTHRA = Formation(
    id=176,
    members=[
        FormationMember(CHEWYEnemy, 151, 111),
        FormationMember(CHEWYEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0177_FORM0179_TWO_CHEWY_TWO_GECKIT_ONE_KRIFFID = Formation(
    id=177,
    members=[
        FormationMember(CHEWYEnemy, 135, 119),
        FormationMember(CHEWYEnemy, 199, 151),
        FormationMember(SHYAWAYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0178_FORM0180_GECKIT_SPINTHRA = Formation(
    id=178,
    members=[
        FormationMember(CHEWYEnemy, 151, 111),
        FormationMember(SPINTHRAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0179_FORM0181_TWO_GECKIT_ONE_SPINTHRA = Formation(
    id=179,
    members=[
        FormationMember(CHEWYEnemy, 183, 151),
        FormationMember(CHEWYEnemy, 135, 127),
        FormationMember(GECKITEnemy, 231, 143),
        FormationMember(GECKITEnemy, 151, 103),
        FormationMember(KRIFFIDEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0180_FORM0182_TWO_GECKIT_TWO_CHEWY_ONE_SHYAWAY = Formation(
    id=180,
    members=[
        FormationMember(GECKITEnemy, 199, 151),
        FormationMember(SPINTHRAEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0181_FORM0183_TWO_GECKIT_SPINTHRA_KRIFFID = Formation(
    id=181,
    members=[
        FormationMember(GECKITEnemy, 183, 135),
        FormationMember(GECKITEnemy, 215, 151),
        FormationMember(SPINTHRAEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0182_FORM0184_BIRDY_HEAVYTROOPA = Formation(
    id=182,
    members=[
        FormationMember(GECKITEnemy, 151, 127),
        FormationMember(GECKITEnemy, 183, 143),
        FormationMember(CHEWYEnemy, 167, 103),
        FormationMember(CHEWYEnemy, 231, 135),
        FormationMember(SHYAWAYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0183_FORM0185_THREE_BIRDY = Formation(
    id=183,
    members=[
        FormationMember(GECKITEnemy, 151, 127),
        FormationMember(GECKITEnemy, 183, 143),
        FormationMember(SPINTHRAEnemy, 151, 103),
        FormationMember(KRIFFIDEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0184_FORM0186_TWO_BIRDY_ONE_HEAVYTROOPA = Formation(
    id=184,
    members=[
        FormationMember(BIRDYEnemy, 135, 119),
        FormationMember(HEAVYTROOPAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0185_FORM0187_FIVE_BIRDY = Formation(
    id=185,
    members=[
        FormationMember(BIRDYEnemy, 215, 119),
        FormationMember(BIRDYEnemy, 151, 119),
        FormationMember(BIRDYEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0186_FORM0188_TWO_BLUEBIRD = Formation(
    id=186,
    members=[
        FormationMember(BIRDYEnemy, 199, 151),
        FormationMember(BIRDYEnemy, 135, 119),
        FormationMember(HEAVYTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0187_FORM0189_TWO_BLUEBIRD_ONE_HEAVYTROOPA = Formation(
    id=187,
    members=[
        FormationMember(BIRDYEnemy, 151, 111),
        FormationMember(BIRDYEnemy, 215, 143),
        FormationMember(BIRDYEnemy, 151, 143),
        FormationMember(BIRDYEnemy, 215, 111),
        FormationMember(BIRDYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0188_FORM0190_FOUR_BLUEBIRD = Formation(
    id=188,
    members=[
        FormationMember(BLUEBIRDEnemy, 199, 151),
        FormationMember(BLUEBIRDEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0189_FORM0191_TWO_BLUEBIRD_ONE_HEAVYTROOPA_2 = Formation(
    id=189,
    members=[
        FormationMember(BLUEBIRDEnemy, 167, 103),
        FormationMember(BLUEBIRDEnemy, 231, 135),
        FormationMember(HEAVYTROOPAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0190_FORM0192_ONE_PINWHEEL = Formation(
    id=190,
    members=[
        FormationMember(BLUEBIRDEnemy, 183, 143),
        FormationMember(BLUEBIRDEnemy, 183, 111),
        FormationMember(BLUEBIRDEnemy, 231, 135),
        FormationMember(BLUEBIRDEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0191_FORM0193_PINWHEEL_MUCKLE = Formation(
    id=191,
    members=[
        FormationMember(BLUEBIRDEnemy, 151, 111),
        FormationMember(BLUEBIRDEnemy, 215, 143),
        None,
        None,
        FormationMember(HEAVYTROOPAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0192_FORM0194_TWO_PINWHEEL_TWO_MUCKLE = Formation(
    id=192,
    members=[
        FormationMember(PINWHEELEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0193_FORM0195_THREE_PINWHEEL_TWO_SLINGSHY = Formation(
    id=193,
    members=[
        FormationMember(PINWHEELEnemy, 135, 119),
        FormationMember(MUCKLEEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0194_FORM0196_TWO_SHAMAN = Formation(
    id=194,
    members=[
        FormationMember(PINWHEELEnemy, 151, 127),
        FormationMember(PINWHEELEnemy, 183, 143),
        FormationMember(MUCKLEEnemy, 151, 103),
        FormationMember(MUCKLEEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0195_FORM0197_SHAMAN_ORBISON_JAWFUL = Formation(
    id=195,
    members=[
        FormationMember(PINWHEELEnemy, 151, 143),
        FormationMember(PINWHEELEnemy, 135, 119),
        FormationMember(PINWHEELEnemy, 199, 151),
        FormationMember(SLINGSHYEnemy, 167, 111),
        FormationMember(SLINGSHYEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0196_FORM0198_TWO_SHAMAN_ONE_JAWFUL = Formation(
    id=196,
    members=[
        FormationMember(SHAMANEnemy, 151, 111),
        FormationMember(SHAMANEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0197_FORM0199_TWO_SHAMAN_TWO_SLINGSHY_JAWFUL = Formation(
    id=197,
    members=[
        FormationMember(SHAMANEnemy, 135, 119),
        FormationMember(ORBISONEnemy, 199, 151),
        FormationMember(JAWFULEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0198_FORM0200_SLINGSHY_ORBISON = Formation(
    id=198,
    members=[
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
        FormationMember(JAWFULEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0199_FORM0201_ONE_SLINGSHY_TWO_ORBISON = Formation(
    id=199,
    members=[
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
        FormationMember(SLINGSHYEnemy, 135, 127),
        FormationMember(SLINGSHYEnemy, 183, 151),
        FormationMember(JAWFULEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0200_FORM0202_SLINGSHY_TWO_ORBISON_JAWFUL = Formation(
    id=200,
    members=[
        FormationMember(SLINGSHYEnemy, 135, 119),
        FormationMember(ORBISONEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0201_FORM0203_TWO_SLINGSHY_TWO_PINWHEEL_MUCKLE = Formation(
    id=201,
    members=[
        FormationMember(SLINGSHYEnemy, 183, 127),
        FormationMember(ORBISONEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0202_FORM0204_ONE_MAGMUS = Formation(
    id=202,
    members=[
        FormationMember(SLINGSHYEnemy, 167, 135),
        FormationMember(ORBISONEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 215, 143),
        FormationMember(JAWFULEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0203_FORM0205_TWO_MAGMUS_ONE_ARMOREDANT = Formation(
    id=203,
    members=[
        FormationMember(SLINGSHYEnemy, 183, 143),
        FormationMember(SLINGSHYEnemy, 151, 127),
        FormationMember(PINWHEELEnemy, 151, 111),
        FormationMember(PINWHEELEnemy, 215, 143),
        FormationMember(MUCKLEEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0204_FORM0206_THREE_MAGMUS_TWO_OERLIKON = Formation(
    id=204,
    members=[
        FormationMember(MAGMUSEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0205_FORM0207_TWO_MAGMUS_TWO_ARMOREDANT = Formation(
    id=205,
    members=[
        FormationMember(MAGMUSEnemy, 151, 111),
        FormationMember(MAGMUSEnemy, 215, 143),
        FormationMember(ARMOREDANTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0206_FORM0208_OERLIKON_VOMER = Formation(
    id=206,
    members=[
        FormationMember(MAGMUSEnemy, 151, 103),
        FormationMember(MAGMUSEnemy, 231, 143),
        FormationMember(MAGMUSEnemy, 199, 119),
        FormationMember(OERLIKONEnemy, 151, 127),
        FormationMember(OERLIKONEnemy, 183, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0207_FORM0209_THREE_OERLIKON = Formation(
    id=207,
    members=[
        FormationMember(MAGMUSEnemy, 119, 119),
        FormationMember(MAGMUSEnemy, 167, 143),
        FormationMember(ARMOREDANTEnemy, 167, 111),
        FormationMember(ARMOREDANTEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0208_FORM0210_OERLIKON_CHAINEDKONG_ARMOREDANT = Formation(
    id=208,
    members=[
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(VOMEREnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0209_FORM0211_TWO_OERLIKON_ONE_CHAINEDKONG = Formation(
    id=209,
    members=[
        FormationMember(OERLIKONEnemy, 183, 127),
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(OERLIKONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0210_FORM0212_THREE_PYROSPHERE = Formation(
    id=210,
    members=[
        FormationMember(OERLIKONEnemy, 215, 151),
        FormationMember(CHAINEDKONGEnemy, 183, 127),
        FormationMember(ARMOREDANTEnemy, 135, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0211_FORM0213_TWO_PYROSPHERE_ONE_CHAINEDKONG = Formation(
    id=211,
    members=[
        FormationMember(OERLIKONEnemy, 135, 127),
        FormationMember(OERLIKONEnemy, 183, 151),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0212_FORM0214_CORKPEDITE_BODY_PYROSPHERE = Formation(
    id=212,
    members=[
        FormationMember(PYROSPHEREEnemy, 151, 135),
        FormationMember(PYROSPHEREEnemy, 215, 135),
        FormationMember(PYROSPHEREEnemy, 183, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0213_FORM0215_TWO_PYROSPHERE_ONE_STUMPET = Formation(
    id=213,
    members=[
        FormationMember(PYROSPHEREEnemy, 199, 143),
        FormationMember(PYROSPHEREEnemy, 151, 119),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0214_FORM0216_VOMER_CHAINEDKONG = Formation(
    id=214,
    members=[
        FormationMember(CORKPEDITEEnemy, 135, 119),
        FormationMember(BODYEnemy, 151, 111),
        FormationMember(PYROSPHEREEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0215_FORM0217_THREE_VOMER = Formation(
    id=215,
    members=[
        FormationMember(PYROSPHEREEnemy, 199, 151),
        FormationMember(PYROSPHEREEnemy, 199, 119),
        FormationMember(STUMPETEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0216_FORM0218_CORKPEDITE_BODY_VOMER = Formation(
    id=216,
    members=[
        FormationMember(VOMEREnemy, 151, 111),
        FormationMember(CHAINEDKONGEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0217_FORM0219_TWO_VOMER_ONE_STUMPET = Formation(
    id=217,
    members=[
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(VOMEREnemy, 183, 127),
        FormationMember(VOMEREnemy, 215, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0218_FORM0220_ONE_TERRACOTTA = Formation(
    id=218,
    members=[
        FormationMember(CORKPEDITEEnemy, 199, 151),
        FormationMember(BODYEnemy, 215, 143),
        FormationMember(VOMEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0219_FORM0221_THREE_TERRACOTTA = Formation(
    id=219,
    members=[
        FormationMember(VOMEREnemy, 151, 135),
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(STUMPETEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0220_FORM0222_ONE_TERRACOTTA_TWO_FORKIES = Formation(
    id=220,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0221_FORM0223_TWO_TERRACOTTA_TWO_GUGOOMBA_ONE_FORKIES = Formation(
    id=221,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(TERRACOTTAEnemy, 151, 119),
        FormationMember(TERRACOTTAEnemy, 215, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0222_FORM0224_MALAKOOPA_TUBOTROOPA = Formation(
    id=222,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 127),
        FormationMember(FORKIESEnemy, 151, 111),
        FormationMember(FORKIESEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0223_FORM0225_TWO_MALAKOOPA_ONE_TUBOTROOPA = Formation(
    id=223,
    members=[
        FormationMember(TERRACOTTAEnemy, 135, 127),
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(GUGOOMBAEnemy, 231, 135),
        FormationMember(GUGOOMBAEnemy, 167, 103),
        FormationMember(FORKIESEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0224_FORM0226_TWO_MALAKOOPA_TERRACOTTA_TUBOTROOPA = Formation(
    id=224,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 127),
        FormationMember(TUBOTROOPAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0225_FORM0227_ONE_MALAKOOPA_TWO_TUBOTROOPA = Formation(
    id=225,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 119),
        FormationMember(MALAKOOPAEnemy, 199, 151),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0226_FORM0228_TWO_GUGOOMBA = Formation(
    id=226,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 103),
        FormationMember(MALAKOOPAEnemy, 231, 151),
        FormationMember(TERRACOTTAEnemy, 167, 135),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0227_FORM0229_TWO_GUGOOMBA_ONE_STARCRUSTER = Formation(
    id=227,
    members=[
        FormationMember(MALAKOOPAEnemy, 183, 127),
        None,
        None,
        FormationMember(TUBOTROOPAEnemy, 135, 103),
        FormationMember(TUBOTROOPAEnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0228_FORM0230_GUGOOMBA_FORKIES_STARCRUSTER = Formation(
    id=228,
    members=[
        FormationMember(GUGOOMBAEnemy, 151, 111),
        FormationMember(GUGOOMBAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0229_FORM0231_TWO_GUGOOMBA_TWO_MALAKOOPA_TWO_TERRACOTTA = Formation(
    id=229,
    members=[
        FormationMember(GUGOOMBAEnemy, 231, 151),
        FormationMember(GUGOOMBAEnemy, 135, 103),
        FormationMember(STARCRUSTEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0230_FORM0232_ONE_BIGBERTHA = Formation(
    id=230,
    members=[
        FormationMember(GUGOOMBAEnemy, 231, 143),
        FormationMember(FORKIESEnemy, 199, 119),
        FormationMember(STARCRUSTEREnemy, 151, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0231_FORM0233_TWO_BIGBERTHA = Formation(
    id=231,
    members=[
        FormationMember(GUGOOMBAEnemy, 199, 151),
        FormationMember(GUGOOMBAEnemy, 135, 119),
        FormationMember(MALAKOOPAEnemy, 167, 135),
        FormationMember(MALAKOOPAEnemy, 199, 119),
        FormationMember(TERRACOTTAEnemy, 167, 103),
        FormationMember(TERRACOTTAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0232_FORM0234_BIGBERTHA_FORKIES = Formation(
    id=232,
    members=[
        FormationMember(BIGBERTHAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0233_FORM0235_TWO_BIGBERTHA_ONE_TERRACOTTA = Formation(
    id=233,
    members=[
        FormationMember(BIGBERTHAEnemy, 151, 111),
        FormationMember(BIGBERTHAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0234_FORM0236 = Formation(
    id=234,
    members=[
        FormationMember(BIGBERTHAEnemy, 215, 143),
        FormationMember(FORKIESEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0235_FORM0237 = Formation(
    id=235,
    members=[
        FormationMember(BIGBERTHAEnemy, 135, 111),
        FormationMember(BIGBERTHAEnemy, 215, 151),
        FormationMember(TERRACOTTAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0236_FORM0238 = Formation(
    id=236,
    members=[
        FormationMember(MAGIKOOPAEnemy, 199, 119),
        FormationMember(TERRACOTTAEnemy, 135, 103, hidden_at_start=True),
        FormationMember(TERRACOTTAEnemy, 231, 151, hidden_at_start=True),
        FormationMember(TERRACOTTAEnemy, 135, 127, hidden_at_start=True),
        FormationMember(TERRACOTTAEnemy, 183, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
)

FORM0237_FORM0239 = Formation(
    id=237,
    members=[
        FormationMember(MAGIKOOPAEnemy, 199, 119),
        FormationMember(MALAKOOPAEnemy, 215, 143, hidden_at_start=True),
        FormationMember(MALAKOOPAEnemy, 151, 111, hidden_at_start=True),
        FormationMember(TUBOTROOPAEnemy, 167, 135, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
)

FORM0238_FORM0240_ONE_NINJA = Formation(
    id=238,
    members=[
        FormationMember(MAGIKOOPAEnemy, 199, 119),
        FormationMember(GUGOOMBAEnemy, 119, 119, hidden_at_start=True),
        FormationMember(GUGOOMBAEnemy, 199, 159, hidden_at_start=True),
        FormationMember(STARCRUSTEREnemy, 167, 135, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
)

FORM0239_FORM0241_NINJA_DOPPEL = Formation(
    id=239,
    members=[
        FormationMember(MAGIKOOPAEnemy, 199, 119),
        FormationMember(FORKIESEnemy, 135, 111, hidden_at_start=True),
        FormationMember(STARCRUSTEREnemy, 215, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
)

FORM0240_FORM0242_TWO_NINJA_ONE_HIPPOPO = Formation(
    id=240,
    members=[
        FormationMember(NINJAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0241_FORM0243_FIVE_NINJA = Formation(
    id=241,
    members=[
        FormationMember(NINJAEnemy, 151, 119),
        FormationMember(DOPPELEnemy, 199, 159),
    ],
    music=NormalBattleMusic(),
)

FORM0242_FORM0244_SPRINGER_GLUMREAPER = Formation(
    id=242,
    members=[
        FormationMember(NINJAEnemy, 199, 151),
        FormationMember(NINJAEnemy, 135, 119),
        FormationMember(HIPPOPOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0243_FORM0235 = Formation(
    id=243,
    members=[
        FormationMember(NINJAEnemy, 135, 119),
        FormationMember(NINJAEnemy, 183, 127),
        FormationMember(NINJAEnemy, 167, 103),
        FormationMember(NINJAEnemy, 231, 135),
        FormationMember(NINJAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0244_FORM0246_TWO_SPRINGER_ONE_PUPPOX = Formation(
    id=244,
    members=[
        FormationMember(SPRINGEREnemy, 215, 143),
        FormationMember(GLUMREAPEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0246_FORM0248_FIVE_AMEBOID = Formation(
    id=246,
    members=[
        FormationMember(SPRINGEREnemy, 231, 135),
        FormationMember(SPRINGEREnemy, 167, 103),
        FormationMember(PUPPOXEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0247_FORM0249 = Formation(
    id=247,
    members=[
        FormationMember(SPRINGEREnemy, 183, 127),
        FormationMember(PUPPOXEnemy, 215, 143),
        FormationMember(PUPPOXEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0248_FORM0250 = Formation(
    id=248,
    members=[
        FormationMember(AMEBOIDEnemy, 183, 127),
        FormationMember(AMEBOIDEnemy, 167, 103, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 135, 119, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 231, 135, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 199, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
)

FORM0252_FORM0254_TWO_GLUMREAPER_TWO_DOPPEL = Formation(
    id=252,
    members=[
        FormationMember(GLUMREAPEREnemy, 183, 127),
        FormationMember(GLUMREAPEREnemy, 135, 119),
        FormationMember(GLUMREAPEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0253_FORM0255_TWO_GLUMREAPER_TWO_LILBOO = Formation(
    id=253,
    members=[
        FormationMember(GLUMREAPEREnemy, 215, 159),
        FormationMember(HIPPOPOEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0254_FORM0256_ONE_LILBOO = Formation(
    id=254,
    members=[
        FormationMember(GLUMREAPEREnemy, 151, 127),
        FormationMember(GLUMREAPEREnemy, 183, 143),
        FormationMember(DOPPELEnemy, 167, 103),
        FormationMember(DOPPELEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0255_FORM0257_TWO_LILBOO_ONE_HIPPOPO = Formation(
    id=255,
    members=[
        FormationMember(GLUMREAPEREnemy, 135, 111),
        FormationMember(GLUMREAPEREnemy, 215, 151),
        FormationMember(LILBOOEnemy, 167, 135),
        FormationMember(LILBOOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0256_FORM0258_TWO_LILBOO_PUPPOX_DOPPEL = Formation(
    id=256,
    members=[
        FormationMember(LILBOOEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0257_FORM0259_FOUR_LILBOO = Formation(
    id=257,
    members=[
        FormationMember(LILBOOEnemy, 183, 151),
        FormationMember(LILBOOEnemy, 215, 135),
        FormationMember(HIPPOPOEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
)

FORM0258_FORM0260_TWO_MADMALLET = Formation(
    id=258,
    members=[
        FormationMember(LILBOOEnemy, 167, 143),
        FormationMember(LILBOOEnemy, 199, 119),
        FormationMember(PUPPOXEnemy, 151, 103),
        FormationMember(DOPPELEnemy, 215, 159),
    ],
    music=NormalBattleMusic(),
)

FORM0259_FORM0261_THREE_MADMALLET = Formation(
    id=259,
    members=[
        FormationMember(LILBOOEnemy, 167, 135),
        FormationMember(LILBOOEnemy, 151, 111),
        FormationMember(LILBOOEnemy, 215, 143),
        FormationMember(LILBOOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0260_FORM0262_FIVE_MADMALLET = Formation(
    id=260,
    members=[
        FormationMember(MADMALLETEnemy, 151, 119),
        FormationMember(MADMALLETEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0261_FORM0263_THREE_MADMALLET_HENCHMEN = Formation(
    id=261,
    members=[
        FormationMember(MADMALLETEnemy, 151, 127),
        FormationMember(MADMALLETEnemy, 199, 151),
        FormationMember(MADMALLETEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0262_FORM0264_ONE_POUNDER = Formation(
    id=262,
    members=[
        FormationMember(MADMALLETEnemy, 183, 127),
        FormationMember(MADMALLETEnemy, 135, 127),
        FormationMember(MADMALLETEnemy, 231, 135),
        FormationMember(MADMALLETEnemy, 167, 103),
        FormationMember(MADMALLETEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0264_FORM0266_FIVE_POUNDER = Formation(
    id=264,
    members=[
        FormationMember(POUNDEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0265_FORM0267 = Formation(
    id=265,
    members=[
        FormationMember(POUNDEREnemy, 183, 127),
        FormationMember(POUNDEREnemy, 231, 135),
        FormationMember(POUNDEREnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
)

FORM0266_FORM0268_PANDORITE_BOSS_FIGHT = Formation(
    id=266,
    members=[
        FormationMember(POUNDEREnemy, 167, 135),
        FormationMember(POUNDEREnemy, 199, 143),
        FormationMember(POUNDEREnemy, 151, 119),
        FormationMember(POUNDEREnemy, 167, 103),
        FormationMember(POUNDEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0268_FORM0270_BOXBOY_BOSS_FIGHT = Formation(
    id=268,
    members=[
        FormationMember(PANDORITEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0269_FORM0271_CHESTER_BOSS_FIGHT = Formation(
    id=269,
    members=[
        FormationMember(HIDONEnemy, 167, 119),
        FormationMember(GOOMBETTEEnemy, 135, 111, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 135, 135, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 167, 151, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 215, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0270_FORM0272_TWO_BLUEBIRD_HENCHMEN = Formation(
    id=270,
    members=[
        FormationMember(BOXBOYEnemy, 183, 127),
        FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0271_FORM0273 = Formation(
    id=271,
    members=[
        FormationMember(CHESTEREnemy, 183, 127),
        FormationMember(BAHAMUTTEnemy, 135, 119, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0272_FORM0274_BOOSTER_BOSS_FIGHT = Formation(
    id=272,
    members=[
        FormationMember(UnnamedEnemyEnemy3, 151, 71),
        FormationMember(KINKLINKEnemy, 66, 115),
        FormationMember(KINKLINKEnemy, 186, 74),
        FormationMember(BOWSEREnemy, 167, 143),
    ],
    music=None,
    can_run_away=False,
    unknown_byte=24,
    unknown_bit=True,
)

FORM0274_FORM0276_SNIFIT_HENCHMAN = Formation(
    id=274,
    members=[
        FormationMember(BOOSTEREnemy, 183, 127),
        FormationMember(SNIFITEnemy2, 135, 119),
        FormationMember(SNIFITEnemy2, 151, 143),
        FormationMember(SNIFITEnemy2, 199, 151),
        FormationMember(Booster1Enemy, 0, 0),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0275_FORM0277_CROCO1_BOSS_FIGHT = Formation(
    id=275,
    members=[
        FormationMember(BOOSTEREnemy2, 183, 127),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0277_FORM0279_FOUR_BLUEBIRD_HENCHMEN = Formation(
    id=277,
    members=[
        FormationMember(CROCOEnemy, 183, 127),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0278_FORM0280_JOHNNY_BOSS_FIGHT = Formation(
    id=278,
    members=[
        FormationMember(CROCOEnemy2, 183, 127),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0279_FORM0281 = Formation(
    id=279,
    members=[
        FormationMember(WINDCRYS3DEnemy, 183, 127),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0280_FORM0282 = Formation(
    id=280,
    members=[
        FormationMember(JOHNNYEnemy2, 183, 127),
        FormationMember(BANDANABLUEEnemy, 135, 111),
        FormationMember(BANDANABLUEEnemy, 135, 135),
        FormationMember(BANDANABLUEEnemy, 183, 159),
        FormationMember(BANDANABLUEEnemy, 215, 151),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0285_FORM0287_BELOME_2_BOSS_FIGHT = Formation(
    id=285,
    members=[
        FormationMember(KINGCALAMARIEnemy, 222, 94, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 136, 115, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 112, 127, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 193, 143, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 168, 156, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 135, 143, hidden_at_start=True),
    ],
    run_event_at_load=26,
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0286_FORM0288 = Formation(
    id=286,
    members=[
        FormationMember(BELOMEEnemy, 183, 127),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0287_FORM0289_VALENTINA_BOSS_FIGHT = Formation(
    id=287,
    members=[
        FormationMember(BELOMEEnemy2, 183, 127),
        FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0288_FORM0290 = Formation(
    id=288,
    members=[
        FormationMember(BELOMEEnemy3, 183, 127),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0289_FORM0291 = Formation(
    id=289,
    members=[
        FormationMember(VALENTINAEnemy, 183, 127),
        FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0293_FORM0295_COUNTDOWN_BOSS_FIGHT = Formation(
    id=293,
    members=[
        FormationMember(CZARDRAGONEnemy, 183, 143),
        FormationMember(ZOMBONEEnemy, 183, 143, hidden_at_start=True),
        FormationMember(HELIOEnemy, 167, 119, hidden_at_start=True),
        FormationMember(HELIOEnemy, 135, 135, hidden_at_start=True),
        FormationMember(HELIOEnemy, 199, 167, hidden_at_start=True),
        FormationMember(HELIOEnemy, 231, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0294_FORM0296 = Formation(
    id=294,
    members=[
        FormationMember(SMILAXEnemy, 180, 157),
        FormationMember(SMILAXEnemy, 164, 175, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 143, 119, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 207, 151, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 191, 127, hidden_at_start=True),
        FormationMember(MEGASMILAXEnemy, 175, 111, hidden_at_start=True),
    ],
    run_event_at_load=58,
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0295_FORM0297_BIRDETTA_BOSS_FIGHT = Formation(
    id=295,
    members=[
        FormationMember(COUNTDOWNEnemy, 150, 93),
        FormationMember(DINGALINGEnemy, 158, 52),
        FormationMember(DINGALINGEnemy, 194, 67),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0297_FORM0299_KGGG_BOSS_FIGHT = Formation(
    id=297,
    members=[
        FormationMember(BIRDOEnemy, 167, 118, hidden_at_start=True),
        FormationMember(SHELLYEnemy, 171, 103),
        FormationMember(EGGBERTEnemy, 135, 119, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 135, 135, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 167, 151, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 199, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0298_FORM0300_HELIO_HENCHMEN = Formation(
    id=298,
    members=[
        FormationMember(BUNDTEnemy2, 199, 127),
        FormationMember(RASPBERRYEnemy2, 199, 119),
        FormationMember(TORTEEnemy2, 199, 151),
        FormationMember(TORTEEnemy2, 135, 119),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0299_FORM0301_JINX_1_BOSS_FIGHT = Formation(
    id=299,
    members=[
        FormationMember(KNIFEGUYEnemy, 151, 119),
        FormationMember(GRATEGUYEnemy, 199, 143),
    ],
    run_event_at_load=17,
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0301_FORM0303_YARIDOVICH_BOSS_FIGHT = Formation(
    id=301,
    members=[
        FormationMember(JINXEnemy4, 183, 127),
    ],
    run_event_at_load=71,
    music=MidbossMusic(),
)

FORM0302_FORM0304_AXEM_BOSS_FIGHT = Formation(
    id=302,
    members=[
        FormationMember(MACKEnemy, 199, 119),
        FormationMember(BODYGUARDEnemy, 135, 111),
        FormationMember(BODYGUARDEnemy, 151, 127),
        FormationMember(BODYGUARDEnemy, 183, 143),
        FormationMember(BODYGUARDEnemy, 215, 151),
    ],
    music=BossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0303_FORM0305_BOWYER_BOSS_FIGHT = Formation(
    id=303,
    members=[
        FormationMember(YARIDOVICHEnemy2, 183, 127),
        FormationMember(YARIDOVICHEnemy, 183, 127, hidden_at_start=True),
    ],
    music=BossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0304_FORM0306 = Formation(
    id=304,
    members=[
        FormationMember(AXEMRANGERSEnemy, 201, 79),
        FormationMember(AXEMREDEnemy, 135, 111, hidden_at_start=True),
        FormationMember(AXEMBLACKEnemy, 135, 127, hidden_at_start=True),
        FormationMember(AXEMPINKEnemy, 151, 143, hidden_at_start=True),
        FormationMember(AXEMGREENEnemy, 183, 151, hidden_at_start=True),
        FormationMember(AXEMYELLOWEnemy, 215, 151, hidden_at_start=True),
    ],
    run_event_at_load=61,
    music=BossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0305_FORM0307_EXOR_BOSS_FIGHT = Formation(
    id=305,
    members=[
        FormationMember(BOWYEREnemy, 183, 127),
    ],
    run_event_at_load=3,
    music=BossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0307_FORM0309_CLOAKER_DOMINO_FIGHT = Formation(
    id=307,
    members=[
        FormationMember(EXOREnemy, 193, 64),
        FormationMember(NEOSQUIDEnemy, 187, 136),
        FormationMember(RIGHTEYEEnemy, 174, 145, hidden_at_start=True),
        FormationMember(LEFTEYEEnemy, 203, 157, hidden_at_start=True),
    ],
    run_event_at_load=80,
    music=BossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0308_FORM0310_THREE_RATFUNK = Formation(
    id=308,
    members=[
        FormationMember(SMITHYEnemy3, 199, 127),
        FormationMember(SMELTEREnemy, 87, 87),
        FormationMember(MACHINEMADEEnemy, 135, 127, hidden_at_start=True),
        FormationMember(MACHINEMADEEnemy, 199, 159, hidden_at_start=True),
    ],
    music=Smithy1Music(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0309_FORM0311_FIVE_RATFUNK = Formation(
    id=309,
    members=[
        FormationMember(CLOAKEREnemy, 151, 111),
        FormationMember(DOMINOEnemy, 215, 159),
        FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
    ],
    run_event_at_load=52,
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0310_FORM0312_ONE_ARTICHOKER = Formation(
    id=310,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(RATFUNKEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0311_FORM0313_TWO_ARTICHOKERS = Formation(
    id=311,
    members=[
        FormationMember(RATFUNKEnemy, 135, 127),
        FormationMember(RATFUNKEnemy, 167, 103),
        FormationMember(RATFUNKEnemy, 183, 151),
        FormationMember(RATFUNKEnemy, 231, 135),
        FormationMember(RATFUNKEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0312_FORM0314_PUNCHINELLO_BOSS_FIGHT = Formation(
    id=312,
    members=[
        FormationMember(ARTICHOKEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0313_FORM0315_HAMMERBRO_BOSS_FIGHT = Formation(
    id=313,
    members=[
        FormationMember(ARTICHOKEREnemy, 151, 119),
        FormationMember(ARTICHOKEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0314_FORM0316_THREE_CROOK_HENCHMEN = Formation(
    id=314,
    members=[
        FormationMember(PUNCHINELLOEnemy2, 199, 119),
        FormationMember(MICROBOMBEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 151, 135, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 183, 151, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 215, 159, hidden_at_start=True),
    ],
    run_event_at_load=14,
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0315_FORM0317_FIVE_CROOK_HENCHMEN = Formation(
    id=315,
    members=[
        FormationMember(HAMMERBROEnemy, 135, 127),
        FormationMember(HAMMERBROEnemy, 199, 143),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0316_FORM0318_ONE_SNIFIT = Formation(
    id=316,
    members=[
        FormationMember(CROOKEnemy, 135, 119),
        FormationMember(CROOKEnemy, 199, 119),
        FormationMember(CROOKEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0317_FORM0319_ONE_STUMPET_TWO_MAGMUS = Formation(
    id=317,
    members=[
        FormationMember(CROOKEnemy, 167, 103),
        FormationMember(CROOKEnemy, 135, 119),
        FormationMember(CROOKEnemy, 183, 127),
        FormationMember(CROOKEnemy, 199, 151),
        FormationMember(CROOKEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0318_FORM0320_ONE_POUNDETTE = Formation(
    id=318,
    members=[
        FormationMember(SNIFITEnemy2, 167, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0319_FORM0321_THREE_POUNDETTES = Formation(
    id=319,
    members=[
        FormationMember(STUMPETEnemy, 183, 127),
        FormationMember(MAGMUSEnemy, 119, 127),
        FormationMember(MAGMUSEnemy, 183, 159),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0320_FORM0322_SIX_POUNDETTES = Formation(
    id=320,
    members=[
        FormationMember(POUNDETTEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0321_FORM0323 = Formation(
    id=321,
    members=[
        FormationMember(POUNDETTEEnemy, 183, 127),
        FormationMember(POUNDETTEEnemy, 151, 111),
        FormationMember(POUNDETTEEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0322_FORM0324_JABIT_MADMALLET = Formation(
    id=322,
    members=[
        FormationMember(POUNDETTEEnemy, 167, 135),
        FormationMember(POUNDETTEEnemy, 199, 119),
        FormationMember(POUNDETTEEnemy, 135, 119),
        FormationMember(POUNDETTEEnemy, 167, 103),
        FormationMember(POUNDETTEEnemy, 199, 151),
        FormationMember(POUNDETTEEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0324_FORM0326_SIX_JABIT = Formation(
    id=324,
    members=[
        FormationMember(JABITEnemy, 215, 135),
        FormationMember(MADMALLETEnemy, 151, 119),
    ],
    music=NormalBattleMusic(),
)

FORM0325_FORM0327_JABITS_MADMALLETS_POUNDETTES = Formation(
    id=325,
    members=[
        FormationMember(JABITEnemy, 151, 143),
        FormationMember(POUNDEREnemy, 151, 111),
        FormationMember(POUNDETTEEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0326_FORM0328_TWO_FIREBALL = Formation(
    id=326,
    members=[
        FormationMember(JABITEnemy, 135, 119),
        FormationMember(JABITEnemy, 167, 135),
        FormationMember(JABITEnemy, 231, 135),
        FormationMember(JABITEnemy, 167, 103),
        FormationMember(JABITEnemy, 199, 119),
        FormationMember(JABITEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0327_FORM0329_THREE_FIREBALL = Formation(
    id=327,
    members=[
        FormationMember(JABITEnemy, 151, 127),
        FormationMember(JABITEnemy, 183, 143),
        FormationMember(MADMALLETEnemy, 135, 103),
        FormationMember(MADMALLETEnemy, 183, 111),
        FormationMember(POUNDETTEEnemy, 215, 127),
        FormationMember(POUNDETTEEnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0328_FORM0330_ONE_STUMPET_THREE_MAGMUS = Formation(
    id=328,
    members=[
        FormationMember(FIREBALLEnemy, 151, 111),
        FormationMember(FIREBALLEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0329_FORM0331_CORKPEDITE_OERLIKON = Formation(
    id=329,
    members=[
        FormationMember(FIREBALLEnemy, 167, 135),
        FormationMember(FIREBALLEnemy, 167, 111),
        FormationMember(FIREBALLEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0330_FORM0332_CORKPEDITE_TWO_OERLIKONS = Formation(
    id=330,
    members=[
        FormationMember(STUMPETEnemy, 151, 111),
        FormationMember(MAGMUSEnemy, 183, 159),
        FormationMember(MAGMUSEnemy, 199, 135),
        FormationMember(MAGMUSEnemy, 231, 159),
    ],
    music=NormalBattleMusic(),
)

FORM0331_FORM0333_JINX_2_BOSS_FIGHT = Formation(
    id=331,
    members=[
        FormationMember(CORKPEDITEEnemy, 151, 111),
        FormationMember(BODYEnemy, 167, 103),
        FormationMember(OERLIKONEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0332_FORM0334_JINX_3_BOSS_FIGHT = Formation(
    id=332,
    members=[
        FormationMember(CORKPEDITEEnemy, 151, 111),
        FormationMember(BODYEnemy, 167, 103),
        FormationMember(OERLIKONEnemy, 183, 159),
        FormationMember(OERLIKONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0333_FORM0335_JAGGER_BOSS_FIGHT = Formation(
    id=333,
    members=[
        FormationMember(JINXEnemy3, 183, 127),
    ],
    run_event_at_load=72,
    music=MidbossMusic(),
)

FORM0334_FORM0336 = Formation(
    id=334,
    members=[
        FormationMember(JINXEnemy4, 183, 127),
    ],
    run_event_at_load=73,
    music=MidbossMusic(),
)

FORM0335_FORM0337 = Formation(
    id=335,
    members=[
        FormationMember(JAGGEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0336_FORM0338 = Formation(
    id=336,
    members=[
    ],
    run_event_at_load=7,
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0337_FORM0339 = Formation(
    id=337,
    members=[
    ],
    run_event_at_load=8,
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0338_FORM0340 = Formation(
    id=338,
    members=[
    ],
    run_event_at_load=29,
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0339_FORM0341 = Formation(
    id=339,
    members=[
    ],
    run_event_at_load=30,
    music=None,
    can_run_away=False,
    unknown_bit=True,
)

FORM0340_FORM0342 = Formation(
    id=340,
    members=[
        FormationMember(SKYTROOPAEnemy, 135, 127),
        FormationMember(SKYTROOPAEnemy, 215, 143),
    ],
    run_event_at_load=37,
    music=None,
)

FORM0341_FORM0343 = Formation(
    id=341,
    members=[
        FormationMember(GOOMBAEnemy, 135, 119),
        FormationMember(GOOMBAEnemy, 199, 151),
        FormationMember(K9Enemy, 199, 119),
    ],
    run_event_at_load=38,
    music=None,
)

FORM0342_FORM0344 = Formation(
    id=342,
    members=[
        FormationMember(THEBIGBOOEnemy, 119, 119),
        FormationMember(THEBIGBOOEnemy, 199, 159),
        FormationMember(SHADOWEnemy, 167, 111),
        FormationMember(SHADOWEnemy, 215, 135),
    ],
    run_event_at_load=39,
    music=None,
)

FORM0343_FORM0345_FIVE_BIRDY_HENCHMEN = Formation(
    id=343,
    members=[
        FormationMember(PIRANHAPLANTEnemy, 167, 135),
        FormationMember(PIRANHAPLANTEnemy, 135, 119),
        FormationMember(PIRANHAPLANTEnemy, 199, 151),
        FormationMember(SPARKYEnemy, 167, 111),
        FormationMember(SPARKYEnemy, 215, 135),
    ],
    run_event_at_load=40,
    music=None,
)

FORM0344_FORM0346_THREE_AXEM_HENCHMEN = Formation(
    id=344,
    members=[
        FormationMember(CORKPEDITEEnemy, 167, 135),
        FormationMember(BODYEnemy, 183, 127),
    ],
    run_event_at_load=41,
    music=None,
)

FORM0345_FORM0347_FOUR_AXEM_HENCHMEN = Formation(
    id=345,
    members=[
        FormationMember(MALLOWCOPYSEnemy, 151, 127),
        FormationMember(MALLOWCOPYSEnemy, 215, 143),
    ],
    music=None,
)

FORM0346_FORM0348_THREE_BLOOBER_HENCHMEN = Formation(
    id=346,
    members=[
        FormationMember(SNIFITEnemy, 167, 118),
    ],
    run_event_at_load=92,
    music=None,
)

FORM0347_FORM0349_TWO_BOWYER_AEROS = Formation(
    id=347,
    members=[
        FormationMember(CULEX3DEnemy, 135, 119),
        FormationMember(CULEX3DEnemy, 151, 135),
        FormationMember(CULEX3DEnemy, 183, 151),
        FormationMember(CULEX3DEnemy, 215, 159),
        FormationMember(CULEX3DEnemy, 199, 119, hidden_at_start=True),
    ],
    music=None,
)

FORM0348_FORM0350_CULEX_BOSS_FIGHT = Formation(
    id=348,
    members=[
        FormationMember(JOHNNYEnemy, 183, 143),
    ],
    music=None,
)

FORM0349_FORM0351_MOKURA_BOSS_FIGHT = Formation(
    id=349,
    members=[
        FormationMember(GOOMBAEnemy, 151, 111),
        FormationMember(GOOMBAEnemy, 167, 135),
        FormationMember(GOOMBAEnemy, 215, 143),
    ],
    run_event_at_load=43,
    music=NormalBattleMusic(),
)

FORM0350_FORM0352_THREE_PYROSPHERE_HENCHMEN = Formation(
    id=350,
    members=[
        FormationMember(CULEXEnemy, 183, 103),
        FormationMember(FIRECRYSTALEnemy, 135, 103, hidden_at_start=True),
        FormationMember(FIRECRYSTALEnemy, 151, 119, hidden_at_start=True),
        FormationMember(FIRECRYSTALEnemy, 183, 135, hidden_at_start=True),
        FormationMember(FIRECRYSTALEnemy, 215, 143, hidden_at_start=True),
    ],
    music=CulexMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0351_FORM0353_ONE_FIRE_CRYSTAL = Formation(
    id=351,
    members=[
        FormationMember(FORMLESSEnemy, 167, 135),
        FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0352_FORM0354_THREE_SHOGUNS = Formation(
    id=352,
    members=[
        FormationMember(PUNCHINELLOEnemy, 167, 135),
        FormationMember(PUNCHINELLOEnemy, 151, 111),
        FormationMember(PUNCHINELLOEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0353_FORM0355_THREE_HEAVY_TROOPA = Formation(
    id=353,
    members=[
        FormationMember(PUNCHINELLOEnemy, 167, 103),
        FormationMember(PUNCHINELLOEnemy, 151, 127),
        FormationMember(PUNCHINELLOEnemy, 215, 127),
        FormationMember(PUNCHINELLOEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0354_FORM0356_DODO_BOSS_FIGHT = Formation(
    id=354,
    members=[
        FormationMember(SHOGUNEnemy, 167, 135),
        FormationMember(SHOGUNEnemy, 151, 111),
        FormationMember(SHOGUNEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0355_FORM0357_KAMEK_BOSS_FIGHT = Formation(
    id=355,
    members=[
        FormationMember(HEAVYTROOPAEnemy, 167, 135),
        FormationMember(HEAVYTROOPAEnemy, 151, 103),
        FormationMember(HEAVYTROOPAEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
)

FORM0356_FORM0358_BOOMER_BOSS_FIGHT = Formation(
    id=356,
    members=[
        FormationMember(DODOEnemy2, 183, 127),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0357_FORM0359_MACHINE_MACK = Formation(
    id=357,
    members=[
        FormationMember(MAGIKOOPAEnemy, 215, 111),
        FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
    ],
    run_event_at_load=101,
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0358_FORM0360_MACHINE_BOWYER = Formation(
    id=358,
    members=[
        FormationMember(BOOMEREnemy, 215, 143),
        FormationMember(HANGINSHYEnemy, 66, 115),
        FormationMember(HANGINSHYEnemy, 186, 74),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0359_FORM0361_MACHINE_YARIDOVICH = Formation(
    id=359,
    members=[
        FormationMember(MACHINEMADEEnemy3, 199, 119),
        FormationMember(MACHINEMADEEnemy, 135, 111),
        FormationMember(MACHINEMADEEnemy, 151, 127),
        FormationMember(MACHINEMADEEnemy, 183, 143),
        FormationMember(MACHINEMADEEnemy, 215, 151),
    ],
    music=BossMusic(),
)

FORM0360_FORM0362_THREE_MACHINE_AXEMS = Formation(
    id=360,
    members=[
        FormationMember(MACHINEMADEEnemy4, 183, 127),
    ],
    music=BossMusic(),
)

FORM0361_FORM0363_SMITHY_2 = Formation(
    id=361,
    members=[
        FormationMember(MACHINEMADEEnemy5, 183, 127),
        FormationMember(MACHINEMADEEnemy2, 135, 119, hidden_at_start=True),
        FormationMember(MACHINEMADEEnemy2, 167, 103, hidden_at_start=True),
        FormationMember(MACHINEMADEEnemy2, 199, 151, hidden_at_start=True),
        FormationMember(MACHINEMADEEnemy2, 231, 135, hidden_at_start=True),
    ],
    music=BossMusic(),
)

FORM0362_FORM0364_CLERK_BOSS_FIGHT = Formation(
    id=362,
    members=[
        FormationMember(MACHINEMADEEnemy6, 151, 111),
        None,
        FormationMember(MACHINEMADEEnemy8, 151, 143),
        None,
        FormationMember(MACHINEMADEEnemy10, 215, 143),
    ],
    music=BossMusic(),
)

FORM0363_FORM0365_MANAGER_BOSS_FIGHT = Formation(
    id=363,
    members=[
        FormationMember(SMITHYEnemy4, 183, 135, hidden_at_start=True),
        FormationMember(SMITHYEnemy5, 183, 175),
    ],
    music=NormalBattleMusic(),
)

FORM0364_FORM0366_DIRECTOR_BOSS_FIGHT = Formation(
    id=364,
    members=[
        FormationMember(CLERKEnemy, 199, 119),
        FormationMember(MADMALLETEnemy, 135, 119),
        FormationMember(MADMALLETEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0365_FORM0367_GUNYOLK_BOSS_FIGHT = Formation(
    id=365,
    members=[
        FormationMember(MANAGEREnemy, 199, 119),
        FormationMember(POUNDEREnemy, 151, 111),
        FormationMember(POUNDEREnemy, 167, 135),
        FormationMember(POUNDEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0366_FORM0368_THREE_MAD_MALLETS = Formation(
    id=366,
    members=[
        FormationMember(DIRECTOREnemy, 183, 127),
        FormationMember(POUNDETTEEnemy, 135, 119),
        FormationMember(POUNDETTEEnemy, 167, 103),
        FormationMember(POUNDETTEEnemy, 199, 151),
        FormationMember(POUNDETTEEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0367_FORM0369_ONE_APPRENTICE = Formation(
    id=367,
    members=[
        FormationMember(GUNYOLKEnemy, 199, 103),
        FormationMember(FACTORYCHIEFEnemy, 231, 151),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0368_FORM0370_FOUR_MACHINE_AXEMS = Formation(
    id=368,
    members=[
        FormationMember(MADMALLETEnemy, 151, 111),
        FormationMember(MADMALLETEnemy, 167, 135),
        FormationMember(MADMALLETEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0369_FORM0371_FOUR_TERRA_COTTA_KEEP = Formation(
    id=369,
    members=[
        FormationMember(APPRENTICEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0370_FORM0372_TWO_OERLIKON_ONE_STARCRUSTER_KEEP = Formation(
    id=370,
    members=[
        FormationMember(MACHINEMADEEnemy7, 151, 119),
        FormationMember(MACHINEMADEEnemy7, 231, 127),
        FormationMember(MACHINEMADEEnemy9, 199, 143),
        FormationMember(MACHINEMADEEnemy9, 183, 103),
    ],
    music=BossMusic(),
)

FORM0371_FORM0373_ONE_SACKIT_TWO_BIGBERTHA_KEEP = Formation(
    id=371,
    members=[
        FormationMember(TERRACOTTAEnemy, 135, 127),
        FormationMember(TERRACOTTAEnemy, 183, 111),
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(TERRACOTTAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0372_FORM0374_ONE_CHOW_TWO_FORKIES_KEEP = Formation(
    id=372,
    members=[
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(OERLIKONEnemy, 199, 151),
        FormationMember(STARCRUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0373_FORM0375_ONE_ALLEYRAT_TWO_ARMOREDANT_KEEP = Formation(
    id=373,
    members=[
        FormationMember(SACKITEnemy, 167, 135),
        None,
        FormationMember(BIGBERTHAEnemy, 151, 103),
        FormationMember(BIGBERTHAEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0374_FORM0376_THREE_BLOOBER_ONE_STARCRUSTER_KEEP = Formation(
    id=374,
    members=[
        FormationMember(CHOWEnemy, 135, 111),
        FormationMember(CHOWEnemy, 215, 151),
        FormationMember(FORKIESEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0375_FORM0377_FOUR_STINGER_KEEP = Formation(
    id=375,
    members=[
        FormationMember(ALLEYRATEnemy, 199, 119),
        FormationMember(ARMOREDANTEnemy, 135, 119),
        FormationMember(ARMOREDANTEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0376_FORM0378_TWO_GECKIT_ONE_CHAINEDKONG_KEEP = Formation(
    id=376,
    members=[
        FormationMember(BLOOBEREnemy, 199, 119),
        FormationMember(BLOOBEREnemy, 183, 151),
        FormationMember(BLOOBEREnemy, 231, 151),
        FormationMember(STARCRUSTEREnemy, 135, 103),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0377_FORM0379_ONE_ROBOMB_TWO_BIGBERTHA_KEEP = Formation(
    id=377,
    members=[
        FormationMember(STINGEREnemy, 151, 111),
        FormationMember(STINGEREnemy, 167, 127),
        FormationMember(STINGEREnemy, 199, 143),
        FormationMember(STINGEREnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0378_FORM0380_FOUR_VOMER_KEEP = Formation(
    id=378,
    members=[
        FormationMember(GECKITEnemy, 215, 151),
        FormationMember(GECKITEnemy, 135, 111),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0379_FORM0381_TWO_MAGMUS_TWO_PULSAR_KEEP = Formation(
    id=379,
    members=[
        FormationMember(ROBOMBEnemy, 167, 135),
        None,
        FormationMember(BIGBERTHAEnemy, 167, 111),
        FormationMember(BIGBERTHAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0380_FORM0382_FIVE_GUGOOMBAS_KEEP = Formation(
    id=380,
    members=[
        FormationMember(VOMEREnemy, 151, 127),
        FormationMember(VOMEREnemy, 183, 143),
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(VOMEREnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0381_FORM0383_TWO_MALAKOOPAS_ONE_TUBOTROOPA_KEEP = Formation(
    id=381,
    members=[
        FormationMember(MAGMUSEnemy, 151, 127),
        FormationMember(MAGMUSEnemy, 183, 143),
        FormationMember(PULSAREnemy, 151, 103),
        FormationMember(PULSAREnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0382_FORM0384_TWO_BIGBOO_TWO_ORBISON_KEEP = Formation(
    id=382,
    members=[
        FormationMember(GUGOOMBAEnemy, 151, 127),
        FormationMember(GUGOOMBAEnemy, 183, 143),
        FormationMember(GUGOOMBAEnemy, 199, 119),
        FormationMember(GUGOOMBAEnemy, 167, 103),
        FormationMember(GUGOOMBAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0383_FORM0385_FIVE_SLINGSHY_KEEP = Formation(
    id=383,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 111),
        FormationMember(MALAKOOPAEnemy, 215, 151),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0384_FORM0386_TWO_CHEWY_TWO_SHYAWAY_KEEP = Formation(
    id=384,
    members=[
        FormationMember(THEBIGBOOEnemy, 183, 143),
        FormationMember(THEBIGBOOEnemy, 151, 127),
        FormationMember(ORBISONEnemy, 167, 103),
        FormationMember(ORBISONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0385_FORM0387_ONE_MRKIPPER_TWO_MUCKLES_KEEP = Formation(
    id=385,
    members=[
        FormationMember(SLINGSHYEnemy, 167, 135),
        FormationMember(SLINGSHYEnemy, 167, 119),
        FormationMember(SLINGSHYEnemy, 199, 135),
        FormationMember(SLINGSHYEnemy, 167, 103),
        FormationMember(SLINGSHYEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0386_FORM0388_TWO_AMANITAS_ONE_ORBISON_KEEP = Formation(
    id=386,
    members=[
        FormationMember(CHEWYEnemy, 151, 127),
        FormationMember(CHEWYEnemy, 183, 143),
        FormationMember(SHYAWAYEnemy, 167, 103),
        FormationMember(SHYAWAYEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0387_FORM0389_TWO_GREAPERS_ONE_GLUMREAPER_KEEP = Formation(
    id=387,
    members=[
        FormationMember(MRKIPPEREnemy, 167, 135),
        FormationMember(MUCKLEEnemy, 167, 103),
        FormationMember(MUCKLEEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0388_FORM0390_THREE_PYROSPHERE_KEEP = Formation(
    id=388,
    members=[
        FormationMember(AMANITAEnemy, 215, 143),
        FormationMember(AMANITAEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0389_FORM0391_THREE_LAKITU_KEEP = Formation(
    id=389,
    members=[
        FormationMember(GREAPEREnemy, 215, 143),
        FormationMember(GREAPEREnemy, 151, 111),
        FormationMember(GLUMREAPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0390_FORM0392_TWO_ZEOSTAR_TWO_SHAMAN_KEEP = Formation(
    id=390,
    members=[
        FormationMember(PYROSPHEREEnemy, 183, 127),
        FormationMember(PYROSPHEREEnemy, 151, 111),
        FormationMember(PYROSPHEREEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0391_FORM0393_SIX_SHAMANS_KEEP = Formation(
    id=391,
    members=[
        FormationMember(LAKITUEnemy, 183, 127),
        FormationMember(LAKITUEnemy, 151, 111),
        FormationMember(LAKITUEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0392_FORM0394_THREE_MACHINE_SHYSTERS = Formation(
    id=392,
    members=[
        FormationMember(ZEOSTAREnemy, 151, 127),
        FormationMember(ZEOSTAREnemy, 183, 143),
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0393_FORM0395_THREE_MACHINE_DRILLBITS = Formation(
    id=393,
    members=[
        FormationMember(SHAMANEnemy, 135, 119),
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 167, 135),
        FormationMember(SHAMANEnemy, 199, 119),
        FormationMember(SHAMANEnemy, 199, 151),
        FormationMember(SHAMANEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0394_FORM0396 = Formation(
    id=394,
    members=[
        FormationMember(MACHINEMADEEnemy, 199, 119),
        FormationMember(MACHINEMADEEnemy, 135, 119),
        FormationMember(MACHINEMADEEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
)

FORM0395_FORM0397 = Formation(
    id=395,
    members=[
        FormationMember(MACHINEMADEEnemy2, 183, 127),
        FormationMember(MACHINEMADEEnemy2, 167, 103),
        FormationMember(MACHINEMADEEnemy2, 231, 135),
    ],
    music=NormalBattleMusic(),
)

FORM0401_FORM0403 = Formation(
    id=401,
    members=[
        FormationMember(JINXEnemy, 181, 122),
        FormationMember(TeamGaugeEnemy, 36, 200),
    ],
    run_event_at_load=39,
    music=MidbossMusic(),
)

FORM0402_FORM0404 = Formation(
    id=402,
    members=[
        FormationMember(JOHNNYEnemy, 165, 121),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0403_FORM0405_ONE_WATER_CRYSTAL = Formation(
    id=403,
    members=[
        FormationMember(BELOMEEnemy3, 183, 127),
        FormationMember(MARIOCLONESEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL3Enemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0404_FORM0406_ONE_EARTH_CRYSTAL = Formation(
    id=404,
    members=[
        FormationMember(BUNDTEnemy, 199, 127),
        FormationMember(RASPBERRYEnemy, 199, 119),
        FormationMember(TORTEEnemy, 199, 151),
        FormationMember(TORTEEnemy, 135, 119),
        FormationMember(CANDLEEnemy, 0, 0),
    ],
    run_event_at_load=13,
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0405_FORM0407_ONE_WIND_CRYSTAL = Formation(
    id=405,
    members=[
        FormationMember(PUNCHINELLOEnemy, 188, 116),
        FormationMember(BOBOMBEnemy4, 145, 103, hidden_at_start=True),
        FormationMember(BOBOMBEnemy2, 150, 129, hidden_at_start=True),
        FormationMember(BOBOMBEnemy5, 182, 142, hidden_at_start=True),
        FormationMember(BOBOMBEnemy3, 223, 142, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0406_FORM0408_THREE_GOOMBETTES = Formation(
    id=406,
    members=[
        FormationMember(BOOSTEREnemy2, 184, 116),
        FormationMember(SNIFITEnemy, 156, 132),
        FormationMember(SNIFITEnemy, 143, 104),
        FormationMember(SNIFITEnemy, 212, 138),
        FormationMember(booster2Enemy, 0, 0),
    ],
    music=MidbossMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0407_FORM0409_ONE_PIRANHA_HENCHMAN = Formation(
    id=407,
    members=[
        FormationMember(CULEX3DEnemy, 183, 103),
        FormationMember(FIRECRYS3DEnemy, 135, 103, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 151, 119, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 183, 135, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 215, 143, hidden_at_start=True),
    ],
    music=CulexMusic(),
    can_run_away=False,
    unknown_bit=True,
)


# ============================================================================
# Pack Definitions
# ============================================================================

# Initialize packs array with None values
packs: list[FormationPack] = [None] * 256  # type: ignore

packs[PACK000_SNIFIT_FIGHT] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN, FORM0001_FORM0001_FOUR_BOBOMB_HENCHMEN, FORM0002_FORM0002_APPRENTICE_HENCHMAN)
packs[PACK001_BOBOMB_HENCHMEN] = FormationPack(FORM0003_FORM0003, FORM0002_FORM0002_APPRENTICE_HENCHMAN, FORM0001_FORM0001_FOUR_BOBOMB_HENCHMEN)
packs[PACK002_SPIKEYS_AND_TROOPAS] = FormationPack(FORM0004_FORM0004_TWO_SPIKEYS, FORM0005_FORM0005_SPIKEY_AND_TROOPA, FORM0005_FORM0005_SPIKEY_AND_TROOPA)
packs[PACK003_SPIKEYS_AND_FROGS] = FormationPack(FORM0007_FORM0007_THREE_SPIKEYS, FORM0006_FORM0006_TWO_SPIKEYS_FROG, FORM0006_FORM0006_TWO_SPIKEYS_FROG)
packs[PACK004_JUST_TROOPAS] = FormationPack(FORM0008_FORM0008_ONE_TROOPA, FORM0009_FORM0009_TWO_TROOPAS, FORM0009_FORM0009_TWO_TROOPAS)
packs[PACK005_TROOPAS_WITH_FROGS_OR_GOOMBAS] = FormationPack(FORM0011_FORM0011_TWO_TROOPAS_GOOMBA, FORM0010_FORM0010_TWO_TROOPAS_FROG, FORM0009_FORM0009_TWO_TROOPAS)
packs[PACK006_JUST_GOOMBAS] = FormationPack(FORM0012_FORM0012_TWO_GOOMBAS, FORM0013_FORM0013_THREE_GOOMBAS, FORM0012_FORM0012_TWO_GOOMBAS)
packs[PACK007_GOOMBAS_WITH_FROGS_OR_SPIKEYS] = FormationPack(FORM0015_FORM0015_GOOMBA_FROG_SPIKEY, FORM0014_FORM0014_TWO_GOOMBAS_SPIKEY, FORM0013_FORM0013_THREE_GOOMBAS)
packs[PACK008_K9S_WITH_SPIKEYS] = FormationPack(FORM0016_FORM0016_ONE_K9, FORM0017_FORM0017_TWO_K9, FORM0018_FORM0018_TWO_K9_SPIKEY)
packs[PACK009_K9S_WITH_SPIKEYS_OR_FROGS] = FormationPack(FORM0019_FORM0019_ONE_K9_TWO_FROG, FORM0018_FORM0018_TWO_K9_SPIKEY, FORM0017_FORM0017_TWO_K9)
packs[PACK010_REGULAR_SHYSTERS_BIASED_2] = FormationPack(FORM0021_FORM0021_TWO_SHYSTER, FORM0022_FORM0022_THREE_SHYSTER, FORM0021_FORM0021_TWO_SHYSTER)
packs[PACK011_REGULAR_SHYSTERS_BIASED_3] = FormationPack(FORM0021_FORM0021_TWO_SHYSTER, FORM0022_FORM0022_THREE_SHYSTER, FORM0022_FORM0022_THREE_SHYSTER)
packs[PACK012_RATFUNKS_WITH_SHADOW_OR_HOBGOBLIN] = FormationPack(FORM0024_FORM0024_TWO_RATFUNKS, FORM0025_FORM0025_TWO_RATFUNKS_ONE_SHADOW, FORM0026_FORM0026_TWO_RATFUNKS_ONE_HOBGOBLIN)
packs[PACK013_RATFUNKS_ALWAYS_WITH_ONE_OTHER_MONSTER] = FormationPack(FORM0027_FORM0027_ONE_RATFUNK_TWO_HOBGOBLINS, FORM0026_FORM0026_TWO_RATFUNKS_ONE_HOBGOBLIN, FORM0025_FORM0025_TWO_RATFUNKS_ONE_SHADOW)
packs[PACK014_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_1] = FormationPack(FORM0029_FORM0029_ONE_BIGBOO_ONE_SHADOW, FORM0029_FORM0029_ONE_BIGBOO_ONE_SHADOW, FORM0030_FORM0030_BIGBOO_SHADOW_HOBGOBLIN)
packs[PACK015_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_2] = FormationPack(FORM0031_FORM0031_THREE_BIGBOO_ONE_SHADOW, FORM0030_FORM0030_BIGBOO_SHADOW_HOBGOBLIN, FORM0029_FORM0029_ONE_BIGBOO_ONE_SHADOW)
packs[PACK016_MULTIPLE_GOBYS_BIASED_2] = FormationPack(FORM0033_FORM0034_THREE_GOBYS, FORM0033_FORM0034_THREE_GOBYS, FORM0034_FORM0036_TWO_CROOKS)
packs[PACK017_MULTIPLE_GOBYS_BIASED_3] = FormationPack(FORM0034_FORM0036_TWO_CROOKS, FORM0034_FORM0036_TWO_CROOKS, FORM0033_FORM0034_THREE_GOBYS)
packs[PACK018_CROOKS_WITH_SHYGUY_OR_SNAPDRAGON] = FormationPack(FORM0036_FORM0038_ONE_CROOK_TWO_SNAPDRAGONS, FORM0037_FORM0039_CROOK_STARSLAP_ARACHNE, FORM0038_FORM0040_ONE_SHYGUY_HENCHMAN)
packs[PACK019_CROOKS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0039_FORM0041_ONE_SHYGUY_ONE_STARSLAP, FORM0038_FORM0040_ONE_SHYGUY_HENCHMAN, FORM0037_FORM0039_CROOK_STARSLAP_ARACHNE)
packs[PACK020_SHYGUYS_WITH_STARSLAP_OR_SNAPDRAGON] = FormationPack(FORM0041_FORM0043_SHYGUY_CROOK_ARACHNE, FORM0041_FORM0043_SHYGUY_CROOK_ARACHNE, FORM0042_FORM0044_STARSLAP_SHYGUY)
packs[PACK021_SHYGUY_STARSLAP_SNAPDRAGON_CROOK_ARACHNE] = FormationPack(FORM0043_FORM0045_STARSLAP_ARACHNE, FORM0042_FORM0044_STARSLAP_SHYGUY, FORM0041_FORM0043_SHYGUY_CROOK_ARACHNE)
packs[PACK022_STARSLAP_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0044_FORM0046_STARSLAP_TWO_SNAPDRAGONS, FORM0045_FORM0047_FOUR_STARSLAPS, FORM0046_FORM0048_ONE_WIGGLER)
packs[PACK023_STARSLAPS_SOMETIMES_WITH_OTHER_MONSTERS] = FormationPack(FORM0047_FORM0049_ONE_WIGGLER_ONE_AMANITA, FORM0046_FORM0048_ONE_WIGGLER, FORM0045_FORM0047_FOUR_STARSLAPS)
packs[PACK024_WIGGLERS_WITH_AMANITA] = FormationPack(FORM0048_FORM0050_TWO_WIGGLERS, FORM0049_FORM0051_ONE_WIGGLER_ONE_GUERRILLA, FORM0050_FORM0052_TWO_AMANITAS)
packs[PACK025_WIGGLERS_WITH_GUERRILLA_OR_AMANITA] = FormationPack(FORM0051_FORM0053_TWO_AMANITAS_ONE_BUZZER, FORM0050_FORM0052_TWO_AMANITAS, FORM0049_FORM0051_ONE_WIGGLER_ONE_GUERRILLA)
packs[PACK026_AMANITAS_WITH_BUZZER_OR_OCTOLOT] = FormationPack(FORM0052_FORM0054_TWO_AMANITAS_ONE_OCTOLOT, FORM0053_FORM0055_AMANITA_BUZZER_GUERRILLA, FORM0054_FORM0056_BUZZER_OCTOLOT)
packs[PACK027_AMANITAS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0055_FORM0057_TWO_BUZZERS_ONE_AMANITA, FORM0054_FORM0056_BUZZER_OCTOLOT, FORM0053_FORM0055_AMANITA_BUZZER_GUERRILLA)
packs[PACK028_BUZZERS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0056_FORM0058_BUZZER_GUERRILLA, FORM0057_FORM0059_BUZZER_GUERRILLA_2, FORM0058_FORM0060_ONE_SPARKY)
packs[PACK029_BUZZERS_WITH_AMANITA] = FormationPack(FORM0059_FORM0061_TWO_SPARKY_ONE_SHYRANGER, FORM0058_FORM0060_ONE_SPARKY, FORM0057_FORM0059_BUZZER_GUERRILLA_2)
packs[PACK030_SPARKY_WITH_SHYRANGER] = FormationPack(FORM0060_FORM0062_THREE_SPARKY, FORM0061_FORM0063, FORM0062_FORM0064)
packs[PACK031_MULTIPLE_SPARKY_WITH_SHYRANGER] = FormationPack(FORM0062_FORM0064, FORM0062_FORM0064, FORM0061_FORM0063)
packs[PACK032_APPRENTICE_HENCHMAN_FIGHT] = FormationPack(FORM0064_FORM0066, FORM0065_FORM0067, FORM0066_FORM0068_ONE_PIRANHA)
packs[PACK033_UNUSED] = FormationPack(FORM0067_FORM0069_TWO_PIRANHA_ONE_SHYRANGER, FORM0066_FORM0068_ONE_PIRANHA, FORM0065_FORM0067)
packs[PACK034_PIRANHA_WITH_SHYRANGER] = FormationPack(FORM0068_FORM0070_THREE_PIRANHA, FORM0069_FORM0071_FIVE_PIRANHA, FORM0070_FORM0072_ONE_BOBOMB)
packs[PACK035_MULTIPLE_PIRANHA_WITH_SHYRANGER] = FormationPack(FORM0071_FORM0073_TWO_BOBOMB_ONE_CLUSTER, FORM0070_FORM0072_ONE_BOBOMB, FORM0069_FORM0071_FIVE_PIRANHA)
packs[PACK036_BOBOMB_WITH_CLUSTER] = FormationPack(FORM0072_FORM0074_FOUR_BOBOMB, FORM0073_FORM0075_TWO_BOBOMB_ENIGMA_CLUSTER, FORM0074_FORM0076_SPARKY_ENIGMA)
packs[PACK037_BOBOMB_WITH_CLUSTER_SOMETIMES_ENIGMA] = FormationPack(FORM0075_FORM0077_TWO_SPARKY_ONE_BOBOMB, FORM0074_FORM0076_SPARKY_ENIGMA, FORM0073_FORM0075_TWO_BOBOMB_ENIGMA_CLUSTER)
packs[PACK038_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_1] = FormationPack(FORM0076_FORM0078_ONE_SPARKY_TWO_CLUSTER, FORM0077_FORM0079_TWO_SPARKY_TWO_ENIGMA, FORM0078_FORM0080_TWO_MAGMITE)
packs[PACK039_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_2] = FormationPack(FORM0079_FORM0081_MAGMITE_BOBOMB_SPARKY, FORM0078_FORM0080_TWO_MAGMITE, FORM0077_FORM0079_TWO_SPARKY_TWO_ENIGMA)
packs[PACK040_MAGMITES_WITH_SPARKY_BOBOMB_OR_CLUSTER] = FormationPack(FORM0080_FORM0082_TWO_MAGMITE_TWO_CLUSTER, FORM0081_FORM0083_TWO_MAGMITE_BOBOMB_CLUSTER, FORM0082_FORM0084_ONE_LAKITU)
packs[PACK041_MAGMITES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0083_FORM0085_LAKITU_SPIKESTER_ARTICHOKER, FORM0082_FORM0084_ONE_LAKITU, FORM0081_FORM0083_TWO_MAGMITE_BOBOMB_CLUSTER)
packs[PACK042_LAKITU_WITH_SPIKESTER_ARTICHOKER] = FormationPack(FORM0084_FORM0086_THREE_LAKITU, FORM0085_FORM0087_TWO_LAKITU_ONE_ARTICHOKER, FORM0086_FORM0088_SPIKESTER_CARROBOSCIS)
packs[PACK043_LAKITU_USUALLY_WITH_ARTICHOKER] = FormationPack(FORM0087_FORM0089_TWO_SPIKESTER_ONE_ARTICHOKER, FORM0086_FORM0088_SPIKESTER_CARROBOSCIS, FORM0085_FORM0087_TWO_LAKITU_ONE_ARTICHOKER)
packs[PACK044_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(FORM0088_FORM0090_ONE_SPIKESTER_TWO_CARROBOSCIS, FORM0089_FORM0091_FOUR_SPIKESTER_ONE_CARROBOSCIS, FORM0090_FORM0092_SPOOKUM_ORBUSER)
packs[PACK045_MULTIPLE_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(FORM0091_FORM0093_TWO_SPOOKUM_ONE_JESTER, FORM0090_FORM0092_SPOOKUM_ORBUSER, FORM0089_FORM0091_FOUR_SPIKESTER_ONE_CARROBOSCIS)
packs[PACK046_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(FORM0092_FORM0094_SPOOKUM_REMOCON_ORBUSER, FORM0093_FORM0095_TWO_SPOOKUM_ONE_REMOCON, FORM0094_FORM0096_ONE_ROBOMB)
packs[PACK047_MULTIPLE_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(FORM0095_FORM0097_THREE_ROBOMB, FORM0094_FORM0096_ONE_ROBOMB, FORM0093_FORM0095_TWO_SPOOKUM_ONE_REMOCON)
packs[PACK048_ROBOMB_WITH_REMOCON] = FormationPack(FORM0096_FORM0098_TWO_ROBOMB_ONE_REMOCON, FORM0097_FORM0099_FOUR_ROBOMB_ONE_ORBUSER, FORM0098_FORM0100_CHOMP_JESTER)
packs[PACK049_ROBOMB_WITH_REMOCON_OR_ORBUSER] = FormationPack(FORM0099_FORM0101_CHOMP_ROBOMB_REMOCON, FORM0098_FORM0100_CHOMP_JESTER, FORM0097_FORM0099_FOUR_ROBOMB_ONE_ORBUSER)
packs[PACK050_CHOMP_WITH_OTHER_MONSTERS_1] = FormationPack(FORM0100_FORM0102_TWO_CHOMP_ONE_ORBUSER, FORM0101_FORM0103_ONE_CHOMP_TWO_JESTER, FORM0102_FORM0104_BLASTER_SPOOKUM)
packs[PACK051_CHOMP_WITH_OTHER_MONSTERS_2] = FormationPack(FORM0103_FORM0105_BLASTER_SPOOKUM_REMOCON, FORM0102_FORM0104_BLASTER_SPOOKUM, FORM0101_FORM0103_ONE_CHOMP_TWO_JESTER)
packs[PACK052_BLASTERS_AND_SPOOKUMS_1] = FormationPack(FORM0104_FORM0106_TWO_BLASTER_ONE_SPOOKUM, FORM0105_FORM0107_BLASTER_TWO_ROBOMB_TWO_SPOOKUM, FORM0106_FORM0108_ONE_TORTE)
packs[PACK053_BLASTERS_AND_SPOOKUMS_2] = FormationPack(FORM0107_FORM0109_TWO_TORTE, FORM0106_FORM0108_ONE_TORTE, FORM0105_FORM0107_BLASTER_TWO_ROBOMB_TWO_SPOOKUM)
packs[PACK054_TORTES] = FormationPack(FORM0108_FORM0110_THREE_TORTE, FORM0109_FORM0111_FOUR_TORTE, FORM0110_FORM0112_ONE_MUKU)
packs[PACK055_MULTIPLE_TORTES] = FormationPack(FORM0111_FORM0113_TWO_MUKU, FORM0110_FORM0112_ONE_MUKU, FORM0109_FORM0111_FOUR_TORTE)
packs[PACK056_MUKU_PULSAR_GECKO] = FormationPack(FORM0112_FORM0114_TWO_MUKU_ONE_PULSAR, FORM0113_FORM0115_MUKU_PULSAR_GECKO, FORM0114_FORM0116_TWO_SACKIT)
packs[PACK057_MUKU_PULSAR_GECKO_MULTI] = FormationPack(FORM0115_FORM0117_TWO_SACKIT_MUKU_GECKO, FORM0114_FORM0116_TWO_SACKIT, FORM0113_FORM0115_MUKU_PULSAR_GECKO)
packs[PACK058_SACKIT_WITH_OTHER_MONSTERS] = FormationPack(FORM0116_FORM0118_ONE_SACKIT_TWO_PULSAR, FORM0117_FORM0119_SACKIT_MASTADOOM, FORM0118_FORM0120_GECKO_SACKIT)
packs[PACK059_SACKIT_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0119_FORM0121_GECKO_MASTADOOM, FORM0118_FORM0120_GECKO_SACKIT, FORM0117_FORM0119_SACKIT_MASTADOOM)
packs[PACK060_GECKO_PACK_1] = FormationPack(FORM0120_FORM0122_TWO_GECKO_TWO_MUKU_TWO_SACKIT, FORM0121_FORM0123_TWO_GECKO_ONE_MASTADOOM, FORM0122_FORM0124_TWO_ZEOSTAR)
packs[PACK061_GECKO_PACK_2] = FormationPack(FORM0123_FORM0125_TWO_ZEOSTAR_ONE_BLOOBER, FORM0122_FORM0124_TWO_ZEOSTAR, FORM0121_FORM0123_TWO_GECKO_ONE_MASTADOOM)
packs[PACK062_ZEOSTAR_WITH_BLOOBER_OR_LEUKO] = FormationPack(FORM0124_FORM0126_TWO_ZEOSTAR_TWO_LEUKO, FORM0125_FORM0127_ZEOSTAR_LEUKO_CRUSTY, FORM0126_FORM0128_BLOOPER_KIPPER)
packs[PACK063_ZEOSTAR_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0127_FORM0129_THREE_BLOOBER, FORM0126_FORM0128_BLOOPER_KIPPER, FORM0125_FORM0127_ZEOSTAR_LEUKO_CRUSTY)
packs[PACK064_BLOOBER_PACK_1] = FormationPack(FORM0128_FORM0130_TWO_BLOOBER_KIPPER_CRUSTY, FORM0129_FORM0131_TWO_BLOOBER_TWO_ZEOSTAR_ONE_LEUKO, FORM0130_FORM0132_THREE_KIPPER)
packs[PACK065_BLOOBER_PACK_2] = FormationPack(FORM0131_FORM0133_TWO_KIPPER_ONE_CRUSTY, FORM0130_FORM0132_THREE_KIPPER, FORM0129_FORM0131_TWO_BLOOBER_TWO_ZEOSTAR_ONE_LEUKO)
packs[PACK066_KIPPER_PACK_1] = FormationPack(FORM0132_FORM0134_TWO_KIPPER_ONE_CRUSTY_2, FORM0133_FORM0135_FOUR_KIPPER, FORM0134_FORM0136_FOUR_BANDANA_RED)
packs[PACK067_KIPPER_PACK_2] = FormationPack(FORM0135_FORM0137_FIVE_BANDANA_RED, FORM0134_FORM0136_FOUR_BANDANA_RED, FORM0133_FORM0135_FOUR_KIPPER)
packs[PACK068_BANDANA_REDS_1] = FormationPack(FORM0136_FORM0138)
packs[PACK069_BANDANA_REDS_2] = FormationPack(FORM0137_FORM0139)
packs[PACK070_BANDANA_BLUES] = FormationPack(FORM0140_FORM0142_FOUR_BANDANABLUE, FORM0141_FORM0143_FIVE_BANDANARED_HENCHMEN, FORM0142_FORM0144_TWO_DRYBONES)
packs[PACK071_BANDANA_RED_HENCHMEN] = FormationPack(FORM0143_FORM0145_TWO_DRYBONES_ONE_GREAPER, FORM0142_FORM0144_TWO_DRYBONES, FORM0141_FORM0143_FIVE_BANDANARED_HENCHMEN)
packs[PACK072_DRYBONES_WITH_GREAPER_REACHER] = FormationPack(FORM0144_FORM0146_DRYBONES_GREAPER_REACHER, FORM0145_FORM0147_TWO_DRYBONES_TWO_GREAPER_ONE_REACHER, FORM0146_FORM0148_ALLEYRAT_GORGON)
packs[PACK073_DRYBONES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0147_FORM0149_TWO_ALLEYRAT_TWO_GREAPER, FORM0146_FORM0148_ALLEYRAT_GORGON, FORM0145_FORM0147_TWO_DRYBONES_TWO_GREAPER_ONE_REACHER)
packs[PACK074_ALLEYRAT_PACK_1] = FormationPack(FORM0148_FORM0150_TWO_ALLEYRAT_TWO_GORGON, FORM0149_FORM0151_ALLEYRAT_REACHER_GORGON, FORM0150_FORM0152_ONE_GREAPER)
packs[PACK075_ALLEYRAT_PACK_2] = FormationPack(FORM0151_FORM0153_TWO_GREAPER_ONE_REACHER, FORM0150_FORM0152_ONE_GREAPER, FORM0149_FORM0151_ALLEYRAT_REACHER_GORGON)
packs[PACK076_GREAPER_WITH_REACHER_STRAWHEAD] = FormationPack(FORM0152_FORM0154_GREAPER_STRAWHEAD_REACHER, FORM0153_FORM0155_GREAPER_GORGON_TWO_STRAWHEAD, FORM0154_FORM0156_ONE_DRILLBIT)
packs[PACK077_GREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0155_FORM0157_TWO_DRILLBIT, FORM0154_FORM0156_ONE_DRILLBIT, FORM0153_FORM0155_GREAPER_GORGON_TWO_STRAWHEAD)
packs[PACK078_DRILLBIT_PACK_1] = FormationPack(FORM0156_FORM0158_THREE_DRILLBIT, FORM0157_FORM0159_FIVE_DRILLBIT, FORM0158_FORM0160_STINGER_FINKFLOWER)
packs[PACK079_DRILLBIT_PACK_2] = FormationPack(FORM0159_FORM0161_TWO_STINGER_ONE_OCTOVADER, FORM0158_FORM0160_STINGER_FINKFLOWER, FORM0157_FORM0159_FIVE_DRILLBIT)
packs[PACK080_STINGER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0160_FORM0162_ONE_STINGER_TWO_FINKFLOWER, FORM0161_FORM0163_FOUR_STINGER, FORM0162_FORM0164_CHOW_OCTOVADER)
packs[PACK081_STINGER_WITH_OCTOVADER_OR_FINKFLOWER] = FormationPack(FORM0163_FORM0165_CHOW_SHOGUN, FORM0162_FORM0164_CHOW_OCTOVADER, FORM0161_FORM0163_FOUR_STINGER)
packs[PACK082_CHOW_PACK_1] = FormationPack(FORM0164_FORM0166_CHOW_SHOGUN_OCTOVADER, FORM0165_FORM0167_CHOW_FINKFLOWER_TWO_SHOGUN, FORM0166_FORM0168_ONE_CHOMPCHOMP)
packs[PACK083_CHOW_PACK_2] = FormationPack(FORM0167_FORM0169_TWO_CHOMPCHOMP, FORM0166_FORM0168_ONE_CHOMPCHOMP, FORM0165_FORM0167_CHOW_FINKFLOWER_TWO_SHOGUN)
packs[PACK084_CHOMPCHOMP_PACK_1] = FormationPack(FORM0168_FORM0170_THREE_CHOMPCHOMP, FORM0169_FORM0171_FOUR_CHOMPCHOMP, FORM0170_FORM0172_ONE_SHYAWAY)
packs[PACK085_CHOMPCHOMP_PACK_2] = FormationPack(FORM0171_FORM0173_TWO_SHYAWAY_ONE_KRIFFID, FORM0170_FORM0172_ONE_SHYAWAY, FORM0169_FORM0171_FOUR_CHOMPCHOMP)
packs[PACK086_SHYAWAY_WITH_KRIFFID_OR_RIBBITE] = FormationPack(FORM0172_FORM0174_TWO_SHYAWAY_ONE_RIBBITE, FORM0173_FORM0175_SHYAWAY_GECKIT_RIBBITE, FORM0174_FORM0176_TWO_CHEWY)
packs[PACK087_SHYAWAY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0175_FORM0177_TWO_CHEWY_ONE_SHYAWAY, FORM0174_FORM0176_TWO_CHEWY, FORM0173_FORM0175_SHYAWAY_GECKIT_RIBBITE)
packs[PACK088_CHEWY_WITH_SHYAWAY_OR_SPINTHRA] = FormationPack(FORM0176_FORM0178_CHEWY_SPINTHRA, FORM0177_FORM0179_TWO_CHEWY_TWO_GECKIT_ONE_KRIFFID, FORM0178_FORM0180_GECKIT_SPINTHRA)
packs[PACK089_CHEWY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0179_FORM0181_TWO_GECKIT_ONE_SPINTHRA, FORM0178_FORM0180_GECKIT_SPINTHRA, FORM0177_FORM0179_TWO_CHEWY_TWO_GECKIT_ONE_KRIFFID)
packs[PACK090_GECKIT_PACK_1] = FormationPack(FORM0180_FORM0182_TWO_GECKIT_TWO_CHEWY_ONE_SHYAWAY, FORM0181_FORM0183_TWO_GECKIT_SPINTHRA_KRIFFID, FORM0182_FORM0184_BIRDY_HEAVYTROOPA)
packs[PACK091_GECKIT_PACK_2] = FormationPack(FORM0183_FORM0185_THREE_BIRDY, FORM0182_FORM0184_BIRDY_HEAVYTROOPA, FORM0181_FORM0183_TWO_GECKIT_SPINTHRA_KRIFFID)
packs[PACK092_BIRDY_PACK_1] = FormationPack(FORM0184_FORM0186_TWO_BIRDY_ONE_HEAVYTROOPA, FORM0185_FORM0187_FIVE_BIRDY, FORM0186_FORM0188_TWO_BLUEBIRD)
packs[PACK093_BIRDY_PACK_2] = FormationPack(FORM0187_FORM0189_TWO_BLUEBIRD_ONE_HEAVYTROOPA, FORM0186_FORM0188_TWO_BLUEBIRD, FORM0185_FORM0187_FIVE_BIRDY)
packs[PACK094_BLUEBIRD_PACK_1] = FormationPack(FORM0188_FORM0190_FOUR_BLUEBIRD, FORM0189_FORM0191_TWO_BLUEBIRD_ONE_HEAVYTROOPA_2, FORM0190_FORM0192_ONE_PINWHEEL)
packs[PACK095_BLUEBIRD_PACK_2] = FormationPack(FORM0191_FORM0193_PINWHEEL_MUCKLE, FORM0190_FORM0192_ONE_PINWHEEL, FORM0189_FORM0191_TWO_BLUEBIRD_ONE_HEAVYTROOPA_2)
packs[PACK096_PINWHEEL_WITH_MUCKLE] = FormationPack(FORM0192_FORM0194_TWO_PINWHEEL_TWO_MUCKLE, FORM0193_FORM0195_THREE_PINWHEEL_TWO_SLINGSHY, FORM0194_FORM0196_TWO_SHAMAN)
packs[PACK097_PINWHEEL_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0195_FORM0197_SHAMAN_ORBISON_JAWFUL, FORM0194_FORM0196_TWO_SHAMAN, FORM0193_FORM0195_THREE_PINWHEEL_TWO_SLINGSHY)
packs[PACK098_SHAMAN_WITH_ORBISON_JAWFUL] = FormationPack(FORM0196_FORM0198_TWO_SHAMAN_ONE_JAWFUL, FORM0197_FORM0199_TWO_SHAMAN_TWO_SLINGSHY_JAWFUL, FORM0198_FORM0200_SLINGSHY_ORBISON)
packs[PACK099_SHAMAN_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0199_FORM0201_ONE_SLINGSHY_TWO_ORBISON, FORM0198_FORM0200_SLINGSHY_ORBISON, FORM0197_FORM0199_TWO_SHAMAN_TWO_SLINGSHY_JAWFUL)
packs[PACK100_SLINGSHY_PACK_1] = FormationPack(FORM0200_FORM0202_SLINGSHY_TWO_ORBISON_JAWFUL, FORM0201_FORM0203_TWO_SLINGSHY_TWO_PINWHEEL_MUCKLE, FORM0202_FORM0204_ONE_MAGMUS)
packs[PACK101_SLINGSHY_PACK_2] = FormationPack(FORM0203_FORM0205_TWO_MAGMUS_ONE_ARMOREDANT, FORM0202_FORM0204_ONE_MAGMUS, FORM0201_FORM0203_TWO_SLINGSHY_TWO_PINWHEEL_MUCKLE)
packs[PACK102_MAGMUS_WITH_ARMOREDANT_OERLIKON] = FormationPack(FORM0204_FORM0206_THREE_MAGMUS_TWO_OERLIKON, FORM0205_FORM0207_TWO_MAGMUS_TWO_ARMOREDANT, FORM0206_FORM0208_OERLIKON_VOMER)
packs[PACK103_MAGMUS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0207_FORM0209_THREE_OERLIKON, FORM0206_FORM0208_OERLIKON_VOMER, FORM0205_FORM0207_TWO_MAGMUS_TWO_ARMOREDANT)
packs[PACK104_OERLIKON_PACK_1] = FormationPack(FORM0208_FORM0210_OERLIKON_CHAINEDKONG_ARMOREDANT, FORM0209_FORM0211_TWO_OERLIKON_ONE_CHAINEDKONG, FORM0210_FORM0212_THREE_PYROSPHERE)
packs[PACK105_OERLIKON_PACK_2] = FormationPack(FORM0211_FORM0213_TWO_PYROSPHERE_ONE_CHAINEDKONG, FORM0210_FORM0212_THREE_PYROSPHERE, FORM0209_FORM0211_TWO_OERLIKON_ONE_CHAINEDKONG)
packs[PACK106_PYROSPHERE_WITH_CHAINEDKONG_CORKPEDITE] = FormationPack(FORM0212_FORM0214_CORKPEDITE_BODY_PYROSPHERE, FORM0213_FORM0215_TWO_PYROSPHERE_ONE_STUMPET, FORM0214_FORM0216_VOMER_CHAINEDKONG)
packs[PACK107_PYROSPHERE_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0215_FORM0217_THREE_VOMER, FORM0214_FORM0216_VOMER_CHAINEDKONG, FORM0213_FORM0215_TWO_PYROSPHERE_ONE_STUMPET)
packs[PACK108_VOMER_PACK_1] = FormationPack(FORM0216_FORM0218_CORKPEDITE_BODY_VOMER, FORM0217_FORM0219_TWO_VOMER_ONE_STUMPET, FORM0218_FORM0220_ONE_TERRACOTTA)
packs[PACK109_VOMER_PACK_2] = FormationPack(FORM0219_FORM0221_THREE_TERRACOTTA, FORM0218_FORM0220_ONE_TERRACOTTA, FORM0217_FORM0219_TWO_VOMER_ONE_STUMPET)
packs[PACK110_TERRACOTTA_PACK_1] = FormationPack(FORM0220_FORM0222_ONE_TERRACOTTA_TWO_FORKIES, FORM0221_FORM0223_TWO_TERRACOTTA_TWO_GUGOOMBA_ONE_FORKIES, FORM0222_FORM0224_MALAKOOPA_TUBOTROOPA)
packs[PACK111_TERRACOTTA_PACK_2] = FormationPack(FORM0223_FORM0225_TWO_MALAKOOPA_ONE_TUBOTROOPA, FORM0222_FORM0224_MALAKOOPA_TUBOTROOPA, FORM0221_FORM0223_TWO_TERRACOTTA_TWO_GUGOOMBA_ONE_FORKIES)
packs[PACK112_MALAKOOPA_PACK_1] = FormationPack(FORM0224_FORM0226_TWO_MALAKOOPA_TERRACOTTA_TUBOTROOPA, FORM0225_FORM0227_ONE_MALAKOOPA_TWO_TUBOTROOPA, FORM0226_FORM0228_TWO_GUGOOMBA)
packs[PACK113_MALAKOOPA_PACK_2] = FormationPack(FORM0227_FORM0229_TWO_GUGOOMBA_ONE_STARCRUSTER, FORM0226_FORM0228_TWO_GUGOOMBA, FORM0225_FORM0227_ONE_MALAKOOPA_TWO_TUBOTROOPA)
packs[PACK114_GUGOOMBA_PACK_1] = FormationPack(FORM0228_FORM0230_GUGOOMBA_FORKIES_STARCRUSTER, FORM0229_FORM0231_TWO_GUGOOMBA_TWO_MALAKOOPA_TWO_TERRACOTTA, FORM0230_FORM0232_ONE_BIGBERTHA)
packs[PACK115_GUGOOMBA_PACK_2] = FormationPack(FORM0231_FORM0233_TWO_BIGBERTHA, FORM0230_FORM0232_ONE_BIGBERTHA, FORM0229_FORM0231_TWO_GUGOOMBA_TWO_MALAKOOPA_TWO_TERRACOTTA)
packs[PACK116_BIGBERTHA_PACK_1] = FormationPack(FORM0232_FORM0234_BIGBERTHA_FORKIES, FORM0233_FORM0235_TWO_BIGBERTHA_ONE_TERRACOTTA, FORM0234_FORM0236)
packs[PACK117_BIGBERTHA_PACK_2] = FormationPack(FORM0235_FORM0237, FORM0234_FORM0236, FORM0233_FORM0235_TWO_BIGBERTHA_ONE_TERRACOTTA)
packs[PACK118_MAGIKOOPA_INTRO] = FormationPack(FORM0236_FORM0238, FORM0237_FORM0239, FORM0238_FORM0240_ONE_NINJA)
packs[PACK119_MAGIKOOPA_UNUSED] = FormationPack(FORM0239_FORM0241_NINJA_DOPPEL, FORM0238_FORM0240_ONE_NINJA, FORM0237_FORM0239)
packs[PACK120_NINJA_PACK_1] = FormationPack(FORM0240_FORM0242_TWO_NINJA_ONE_HIPPOPO, FORM0241_FORM0243_FIVE_NINJA, FORM0242_FORM0244_SPRINGER_GLUMREAPER)
packs[PACK121_NINJA_PACK_2] = FormationPack(FORM0243_FORM0235, FORM0242_FORM0244_SPRINGER_GLUMREAPER, FORM0241_FORM0243_FIVE_NINJA)
packs[PACK122_SPRINGER_PACK_1] = FormationPack(FORM0244_FORM0246_TWO_SPRINGER_ONE_PUPPOX, FORM0246_FORM0248_FIVE_AMEBOID, FORM0244_FORM0246_TWO_SPRINGER_ONE_PUPPOX)
packs[PACK123_SPRINGER_PACK_2] = FormationPack(FORM0247_FORM0249, FORM0246_FORM0248_FIVE_AMEBOID, FORM0244_FORM0246_TWO_SPRINGER_ONE_PUPPOX)
packs[PACK124_MADMALLET_PACK_1] = FormationPack(FORM0260_FORM0262_FIVE_MADMALLET, FORM0261_FORM0263_THREE_MADMALLET_HENCHMEN, FORM0262_FORM0264_ONE_POUNDER)
packs[PACK125_MADMALLET_PACK_2] = FormationPack(FORM0262_FORM0264_ONE_POUNDER, FORM0261_FORM0263_THREE_MADMALLET_HENCHMEN, FORM0260_FORM0262_FIVE_MADMALLET)
packs[PACK126_POUNDER_PACK_1] = FormationPack(FORM0264_FORM0266_FIVE_POUNDER, FORM0265_FORM0267, FORM0266_FORM0268_PANDORITE_BOSS_FIGHT)
packs[PACK126_POUNDER_PACK_2] = FormationPack(FORM0266_FORM0268_PANDORITE_BOSS_FIGHT, FORM0265_FORM0267, FORM0264_FORM0266_FIVE_POUNDER)
packs[PACK128_POUNDETTE_PACK_1] = FormationPack(FORM0320_FORM0322_SIX_POUNDETTES, FORM0321_FORM0323, FORM0322_FORM0324_JABIT_MADMALLET)
packs[PACK128_POUNDETTE_PACK_2] = FormationPack(FORM0322_FORM0324_JABIT_MADMALLET, FORM0321_FORM0323, FORM0320_FORM0322_SIX_POUNDETTES)
packs[PACK130_AMEBOIDS] = FormationPack(FORM0248_FORM0250)
packs[PACK131_AMEBOIDS_DUPE] = FormationPack(FORM0248_FORM0250)
packs[PACK132_GLUMREAPER_WITH_HIPPOPO_DOPPEL] = FormationPack(FORM0252_FORM0254_TWO_GLUMREAPER_TWO_DOPPEL, FORM0253_FORM0255_TWO_GLUMREAPER_TWO_LILBOO, FORM0254_FORM0256_ONE_LILBOO)
packs[PACK133_GLUMREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0255_FORM0257_TWO_LILBOO_ONE_HIPPOPO, FORM0254_FORM0256_ONE_LILBOO, FORM0253_FORM0255_TWO_GLUMREAPER_TWO_LILBOO)
packs[PACK134_LILBOO_PACK_1] = FormationPack(FORM0256_FORM0258_TWO_LILBOO_PUPPOX_DOPPEL, FORM0257_FORM0259_FOUR_LILBOO, FORM0258_FORM0260_TWO_MADMALLET)
packs[PACK135_LILBOO_PACK_2] = FormationPack(FORM0259_FORM0261_THREE_MADMALLET, FORM0258_FORM0260_TWO_MADMALLET, FORM0257_FORM0259_FOUR_LILBOO)
packs[PACK136_JABITS_HAMMERS_PACK_1] = FormationPack(FORM0324_FORM0326_SIX_JABIT, FORM0325_FORM0327_JABITS_MADMALLETS_POUNDETTES, FORM0326_FORM0328_TWO_FIREBALL)
packs[PACK137_JABITS_HAMMERS_PACK_2] = FormationPack(FORM0327_FORM0329_THREE_FIREBALL, FORM0326_FORM0328_TWO_FIREBALL, FORM0325_FORM0327_JABITS_MADMALLETS_POUNDETTES)
packs[PACK138_RATFUNKS_ONLY] = FormationPack(FORM0310_FORM0312_ONE_ARTICHOKER, FORM0311_FORM0313_TWO_ARTICHOKERS, FORM0310_FORM0312_ONE_ARTICHOKER)
packs[PACK139_ARTICHOKERS_ONLY] = FormationPack(FORM0312_FORM0314_PUNCHINELLO_BOSS_FIGHT, FORM0313_FORM0315_HAMMERBRO_BOSS_FIGHT, FORM0312_FORM0314_PUNCHINELLO_BOSS_FIGHT)
packs[PACK140_PUNCHINELLO_STATIC] = FormationPack(FORM0314_FORM0316_THREE_CROOK_HENCHMEN)
packs[PACK141_CROOK_HENCHMEN_ONLY] = FormationPack(FORM0316_FORM0318_ONE_SNIFIT, FORM0317_FORM0319_ONE_STUMPET_TWO_MAGMUS, FORM0316_FORM0318_ONE_SNIFIT)
packs[PACK142_SNIFIT_ONLY] = FormationPack(FORM0318_FORM0320_ONE_POUNDETTE)
packs[PACK143_TOWER_FIREBALLS] = FormationPack(FORM0328_FORM0330_ONE_STUMPET_THREE_MAGMUS, FORM0329_FORM0331_CORKPEDITE_OERLIKON, FORM0328_FORM0330_ONE_STUMPET_THREE_MAGMUS)
packs[PACK144_STUMPET_ENCOUNTER] = FormationPack(FORM0319_FORM0321_THREE_POUNDETTES, FORM0330_FORM0332_CORKPEDITE_TWO_OERLIKONS, FORM0319_FORM0321_THREE_POUNDETTES)
packs[PACK145_CORKPEDITE_ENCOUNTER] = FormationPack(FORM0331_FORM0333_JINX_2_BOSS_FIGHT, FORM0332_FORM0334_JINX_3_BOSS_FIGHT, FORM0331_FORM0333_JINX_2_BOSS_FIGHT)
packs[PACK146_CLERK_STATIC] = FormationPack(FORM0364_FORM0366_DIRECTOR_BOSS_FIGHT)
packs[PACK147_MANAGER_STATIC] = FormationPack(FORM0365_FORM0367_GUNYOLK_BOSS_FIGHT)
packs[PACK148_DIRECTOR_STATIC] = FormationPack(FORM0366_FORM0368_THREE_MAD_MALLETS)
packs[PACK149_GUNYOLK_STATIC] = FormationPack(FORM0367_FORM0369_ONE_APPRENTICE)
packs[PACK150_MAD_MALLET_FACTORY_FIGHT] = FormationPack(FORM0368_FORM0370_FOUR_MACHINE_AXEMS)
packs[PACK151_APPRENTICE_FIGHT] = FormationPack(FORM0369_FORM0371_FOUR_TERRA_COTTA_KEEP)
packs[PACK152_THREE_MACHINE_SHYSTER_SUBSTITUTE] = FormationPack(FORM0394_FORM0396)
packs[PACK153_THREE_DRILLBIT_SUBSTITUTE] = FormationPack(FORM0395_FORM0397)
packs[PACK154_SINGLE_SHYGUY_HENCHMAN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK155_MAD_MALLET_HENCHMEN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK156_PANDORITE_FIGHT_STATIC] = FormationPack(FORM0268_FORM0270_BOXBOY_BOSS_FIGHT)
packs[PACK157_HIDON_FIGHT_STATIC] = FormationPack(FORM0269_FORM0271_CHESTER_BOSS_FIGHT)
packs[PACK158_BOXBOY_FIGHT_STATIC] = FormationPack(FORM0270_FORM0272_TWO_BLUEBIRD_HENCHMEN)
packs[PACK159_CHESTER_FIGHT_STATIC] = FormationPack(FORM0271_FORM0273)
packs[PACK160_BOWYER_AERO_HENCHMEN] = FormationPack(FORM0272_FORM0274_BOOSTER_BOSS_FIGHT)
packs[PACK161_BOOSTER_FIGHT_STATIC] = FormationPack(FORM0274_FORM0276_SNIFIT_HENCHMAN)
packs[PACK162_DUMMY_BOOSTER_POSSIBLY_UNUSED] = FormationPack(FORM0275_FORM0277_CROCO1_BOSS_FIGHT)
packs[PACK163_CROCO1_FIGHT_STATIC] = FormationPack(FORM0277_FORM0279_FOUR_BLUEBIRD_HENCHMEN)
packs[PACK164_CROCO2_FIGHT_STATIC] = FormationPack(FORM0278_FORM0280_JOHNNY_BOSS_FIGHT)
packs[PACK165_UNUSED] = FormationPack(FORM0279_FORM0281)
packs[PACK166_JOHNNY_FIGHT_STATIC] = FormationPack(FORM0280_FORM0282)
packs[PACK167_CALAMARI_FIGHT_STATIC] = FormationPack(FORM0285_FORM0287_BELOME_2_BOSS_FIGHT)
packs[PACK168_BELOME1_FIGHT_STATIC] = FormationPack(FORM0286_FORM0288)
packs[PACK169_BELOME2_FIGHT_STATIC] = FormationPack(FORM0287_FORM0289_VALENTINA_BOSS_FIGHT)
packs[PACK170_UNUSED] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK171_VALENTINA_FIGHT_STATIC] = FormationPack(FORM0289_FORM0291)
packs[PACK172_CZAR_FIGHT_STATIC] = FormationPack(FORM0293_FORM0295_COUNTDOWN_BOSS_FIGHT)
packs[PACK173_MEGASMILAX_FIGHT_STATIC] = FormationPack(FORM0294_FORM0296)
packs[PACK174_COUNTDOWN_FIGHT_STATIC] = FormationPack(FORM0295_FORM0297_BIRDETTA_BOSS_FIGHT)
packs[PACK175_BIRDETTA_FIGHT_STATIC] = FormationPack(FORM0297_FORM0299_KGGG_BOSS_FIGHT)
packs[PACK176_BUNDT_FIGHT_STATIC] = FormationPack(FORM0298_FORM0300_HELIO_HENCHMEN)
packs[PACK177_KGGG_FIGHT_STATIC] = FormationPack(FORM0299_FORM0301_JINX_1_BOSS_FIGHT)
packs[PACK178_JINX1_FIGHT_STATIC] = FormationPack(FORM0301_FORM0303_YARIDOVICH_BOSS_FIGHT)
packs[PACK179_MACK_FIGHT_STATIC] = FormationPack(FORM0302_FORM0304_AXEM_BOSS_FIGHT)
packs[PACK180_YARIDOVICH_FIGHT_STATIC] = FormationPack(FORM0303_FORM0305_BOWYER_BOSS_FIGHT)
packs[PACK181_BOWYER_FIGHT_STATIC] = FormationPack(FORM0305_FORM0307_EXOR_BOSS_FIGHT)
packs[PACK182_AXEM_FIGHT_STATIC] = FormationPack(FORM0304_FORM0306)
packs[PACK183_HAMMERBRO_FIGHT_STATIC] = FormationPack(FORM0315_FORM0317_FIVE_CROOK_HENCHMEN)
packs[PACK184_CLOAKER_DOMINO_FIGHT_STATIC] = FormationPack(FORM0309_FORM0311_FIVE_RATFUNK)
packs[PACK185_SMITHY1_FIGHT_STATIC] = FormationPack(FORM0308_FORM0310_THREE_RATFUNK)
packs[PACK186_EXOR_FIGHT_STATIC] = FormationPack(FORM0307_FORM0309_CLOAKER_DOMINO_FIGHT)
packs[PACK187_JINX2_FIGHT_STATIC] = FormationPack(FORM0333_FORM0335_JAGGER_BOSS_FIGHT)
packs[PACK188_JINX3_FIGHT_STATIC] = FormationPack(FORM0334_FORM0336)
packs[PACK189_JAGGER_FIGHT_STATIC] = FormationPack(FORM0335_FORM0337)
packs[PACK190_PYROSPHERE_HENCHMEN] = FormationPack(FORM0352_FORM0354_THREE_SHOGUNS, FORM0353_FORM0355_THREE_HEAVY_TROOPA, FORM0352_FORM0354_THREE_SHOGUNS)
packs[PACK191_HEAVY_TROOPAS] = FormationPack(FORM0355_FORM0357_KAMEK_BOSS_FIGHT)
packs[PACK192_UNUSED] = FormationPack(FORM0336_FORM0338)
packs[PACK193_HELIO_HENCHMEN] = FormationPack(FORM0337_FORM0339)
packs[PACK194_BODYGUARD_PACK_1] = FormationPack(FORM0338_FORM0340)
packs[PACK195_BODYGUARD_PACK_2] = FormationPack(FORM0339_FORM0341)
packs[PACK196_GENO_CLONE_HENCHMAN] = FormationPack(FORM0340_FORM0342)
packs[PACK197_BOWSER_CLONE_HENCHMAN] = FormationPack(FORM0341_FORM0343)
packs[PACK198_TOADSTOOL_CLONE_HENCHMAN] = FormationPack(FORM0342_FORM0344)
packs[PACK199_CROOKS_ONLY] = FormationPack(FORM0343_FORM0345_FIVE_BIRDY_HENCHMEN)
packs[PACK200_MARIO_CLONE_HENCHMAN] = FormationPack(FORM0344_FORM0346_THREE_AXEM_HENCHMEN)
packs[PACK201_BIRDY_HENCHMEN] = FormationPack(FORM0345_FORM0347_FOUR_AXEM_HENCHMEN)
packs[PACK202_MALLOW_CLONE_HENCHMAN] = FormationPack(FORM0346_FORM0348_THREE_BLOOBER_HENCHMEN)
packs[PACK203_MACHINE_AXEM_HENCHMEN] = FormationPack(FORM0347_FORM0349_TWO_BOWYER_AEROS)
packs[PACK204_BLOOBER_HENCHMEN] = FormationPack(FORM0348_FORM0350_CULEX_BOSS_FIGHT)
packs[PACK205_BLUEBIRD_HENCHMEN] = FormationPack(FORM0349_FORM0351_MOKURA_BOSS_FIGHT)
packs[PACK206_DESERT_SHOGUNS] = FormationPack(FORM0354_FORM0356_DODO_BOSS_FIGHT)
packs[PACK207_MOKURA_BOSS_STATIC] = FormationPack(FORM0351_FORM0353_ONE_FIRE_CRYSTAL)
packs[PACK208_DODO_BOSS_STATIC] = FormationPack(FORM0356_FORM0358_BOOMER_BOSS_FIGHT)
packs[PACK209_MAGIKOOPA_BOSS_STATIC] = FormationPack(FORM0357_FORM0359_MACHINE_MACK)
packs[PACK210_BOOMER_BOSS_STATIC] = FormationPack(FORM0358_FORM0360_MACHINE_BOWYER)
packs[PACK211_MACHINE_MACK_PACK] = FormationPack(FORM0359_FORM0361_MACHINE_YARIDOVICH)
packs[PACK212_MACHINE_BOWYER_PACK] = FormationPack(FORM0360_FORM0362_THREE_MACHINE_AXEMS)
packs[PACK213_MACHINE_YARIDOVICH_PACK] = FormationPack(FORM0361_FORM0363_SMITHY_2)
packs[PACK214_FACTORY_MACHINE_AXEMS] = FormationPack(FORM0362_FORM0364_CLERK_BOSS_FIGHT, FORM0370_FORM0372_TWO_OERLIKON_ONE_STARCRUSTER_KEEP, FORM0362_FORM0364_CLERK_BOSS_FIGHT)
packs[PACK215_SMITHY_2_PACK] = FormationPack(FORM0363_FORM0365_MANAGER_BOSS_FIGHT)
packs[PACK216_CULEX_BOSS_STATIC] = FormationPack(FORM0350_FORM0352_THREE_PYROSPHERE_HENCHMEN)
packs[PACK217_FIRE_CRYSTAL_HENCHMAN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK218_WATER_CRYSTAL_HENCHMAN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK219_EARTH_CRYSTAL_HENCHMAN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK220_WIND_CRYSTAL_HENCHMAN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK221_GOOMBETTE_HENCHMEN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK222_PIRANHA_HENCHMEN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK223_EGGBERT_HENCHMEN] = FormationPack(FORM0000_FORM0000_ONE_BOBOMB_HENCHMAN)
packs[PACK224_OBSTACLE_TERRA_COTTA] = FormationPack(FORM0371_FORM0373_ONE_SACKIT_TWO_BIGBERTHA_KEEP)
packs[PACK225_OBSTACLE_OERLIKON] = FormationPack(FORM0372_FORM0374_ONE_CHOW_TWO_FORKIES_KEEP)
packs[PACK226_OBSTACLE_SACKIT] = FormationPack(FORM0373_FORM0375_ONE_ALLEYRAT_TWO_ARMOREDANT_KEEP)
packs[PACK227_OBSTACLE_CHOW] = FormationPack(FORM0374_FORM0376_THREE_BLOOBER_ONE_STARCRUSTER_KEEP)
packs[PACK228_OBSTACLE_ALLEYRAT] = FormationPack(FORM0375_FORM0377_FOUR_STINGER_KEEP)
packs[PACK229_OBSTACLE_BLOOBER] = FormationPack(FORM0376_FORM0378_TWO_GECKIT_ONE_CHAINEDKONG_KEEP)
packs[PACK230_OBSTACLE_STINGER] = FormationPack(FORM0377_FORM0379_ONE_ROBOMB_TWO_BIGBERTHA_KEEP)
packs[PACK231_OBSTACLE_GECKIT] = FormationPack(FORM0378_FORM0380_FOUR_VOMER_KEEP)
packs[PACK232_OBSTACLE_ROBOMB] = FormationPack(FORM0379_FORM0381_TWO_MAGMUS_TWO_PULSAR_KEEP)
packs[PACK233_OBSTACLE_VOMER] = FormationPack(FORM0380_FORM0382_FIVE_GUGOOMBAS_KEEP)
packs[PACK234_OBSTACLE_MAGMUS] = FormationPack(FORM0381_FORM0383_TWO_MALAKOOPAS_ONE_TUBOTROOPA_KEEP)
packs[PACK235_CHESTER_DUPE] = FormationPack(FORM0271_FORM0273)
packs[PACK236_OBSTACLE_GUGOOMBA] = FormationPack(FORM0382_FORM0384_TWO_BIGBOO_TWO_ORBISON_KEEP)
packs[PACK237_OBSTACLE_MALAKOOPA] = FormationPack(FORM0383_FORM0385_FIVE_SLINGSHY_KEEP)
packs[PACK238_OBSTACLE_BIGBOO] = FormationPack(FORM0384_FORM0386_TWO_CHEWY_TWO_SHYAWAY_KEEP)
packs[PACK239_OBSTACLE_SLINGSHY] = FormationPack(FORM0385_FORM0387_ONE_MRKIPPER_TWO_MUCKLES_KEEP)
packs[PACK240_OBSTACLE_CHEWY] = FormationPack(FORM0386_FORM0388_TWO_AMANITAS_ONE_ORBISON_KEEP)
packs[PACK241_OBSTACLE_KIPPER] = FormationPack(FORM0387_FORM0389_TWO_GREAPERS_ONE_GLUMREAPER_KEEP)
packs[PACK242_OBSTACLE_AMANITA] = FormationPack(FORM0388_FORM0390_THREE_PYROSPHERE_KEEP)
packs[PACK243_OBSTACLE_GREAPER] = FormationPack(FORM0389_FORM0391_THREE_LAKITU_KEEP)
packs[PACK244_OBSTACLE_PYROSPHERE] = FormationPack(FORM0390_FORM0392_TWO_ZEOSTAR_TWO_SHAMAN_KEEP)
packs[PACK245_OBSTACLE_LAKITU] = FormationPack(FORM0391_FORM0393_SIX_SHAMANS_KEEP)
packs[PACK246_OBSTACLE_ZEOSTAR] = FormationPack(FORM0392_FORM0394_THREE_MACHINE_SHYSTERS)
packs[PACK247_OBSTACLE_SHAMANS] = FormationPack(FORM0393_FORM0395_THREE_MACHINE_DRILLBITS)
packs[PACK248_AXEM_BLACK_ALONE] = FormationPack(FORM0401_FORM0403)
packs[PACK249_AXEM_PINK_ALONE] = FormationPack(FORM0402_FORM0404)
packs[PACK250_AXEM_YELLOW_ALONE] = FormationPack(FORM0403_FORM0405_ONE_WATER_CRYSTAL)
packs[PACK251_AXEM_GREEN_ALONE] = FormationPack(FORM0404_FORM0406_ONE_EARTH_CRYSTAL)
packs[PACK252_DINGALING_ALONE] = FormationPack(FORM0405_FORM0407_ONE_WIND_CRYSTAL)
packs[PACK253_SMITHY_HENCHMEN_PACK_1] = FormationPack(FORM0406_FORM0408_THREE_GOOMBETTES)
packs[PACK254_SMITHY_HENCHMEN_PACK_2] = FormationPack(FORM0407_FORM0409_ONE_PIRANHA_HENCHMAN)
packs[PACK255_SMITHY_HENCHMEN_PACK_3] = FormationPack(FORM0357_FORM0359_MACHINE_MACK, FORM0100_FORM0102_TWO_CHOMP_ONE_ORBUSER, FORM0288_FORM0290)

# Pack Collection
pack_collection = PackCollection(packs[:256])
