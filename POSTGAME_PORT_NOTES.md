# Postgame Additions — Battle Animation Port — Working Notes

_Last updated: 2026-06-08_

## Decisions (confirmed by user)
- **Scope**: edit battle_animation + formation `run_event_at_load` + monster_ai corrections; produce/verify all needed patches.
- **Cadence**: present cross-source comparison + proposed edits for EACH formation and WAIT for approval before applying.
- **Sprite rule**: monster battle sprite id = monster_id + 256 (postgame names at those slots are stale/auto-generated; trust the id).
- **NO sprite-behaviour/hit-reaction porting** (user): all boss sprites are DUPLICATES of existing sprites, so they already have every animation/sequence they need. Ignore randomizer's bank-35 `bobomb_s` / `*_outsourced` object-sequence machinery — not needed in postgame.
- **Attack/spell/weapon animations are STATIC, one-time shared ports** (don't vary per formation/user). Port each custom enemy attack & spell animation ONCE; same for the 3 weapons. Track which are used as we go; port in a shared pass.

### Revised per-formation work (lighter than first thought)
Per formation = (1) battle/summon EVENTS (script_0x3A6000 + any *_outsourced summon routine, with enemy/sprite remaps), (2) monster AI corrections, (3) sprite refs via +256, (4) start event `run_event_at_load`. NOTHING about sprite behaviours.

## Goal
Port 7 boss fights from **smrpg_web_randomizer** (source of truth) back into the
"Postgame Additions.smc" disassembly at `src/disassembler_output`, by rewriting battle
animation code (+ supporting formation/AI data), then assembling into patch(es).
NO rom disassembly this session — only edit disassembled code that assembles cleanly.

## Key locations
- Working disassembly root: `src/disassembler_output/`
- Battle events + animations: `battle_animation/{02,35,3A}/contents/script_0x*.py`
  - **Battle EVENT queue**: `battle_animation/3A/contents/script_0x3A6000.py`
    - root `DefineObjectQueue(..., identifier="battle_events_root_0x3A6004")` lists events 0..101 (list index = event ID)
    - 2nd root: `battle_events_root_0x3AECF7`
    - each event = `DefineObjectQueue(..., identifier="battle_event_NNNN_...")` + commands + `Jmp`
- Formations: `packs/pack_collection.py` (`Formation` objects; `.run_event_at_load` = start-event id, UInt8|None) → `packassembler`
- Monster AI: `monster_ai/scripts/script_<id>.py` → `battleassembler`
- Enemies: `enemies/enemies.py` (`class XENEMY`, `_monster_id`)
- Attacks: `enemy_attacks/attacks.py`; Spells: `spells/spells.py`; Items: `items/items.py`

- Randomizer (source of truth): `/home/pidge/code/smrpg_web_randomizer/randomizer/`
  - battle_animation: `randomizer/data/battle_animation/_3A/contents/script_0x*.py` (note `_3A`)
  - enemies: `randomizer/data/enemies/enemies.py`
  - monster_ai: `randomizer/data/monster_ai/scripts/script_<id>.py`
  - formations: `randomizer/data/packs/pack_collection.py`
  - start events: `randomizer/progression/prizes.py` (`_force_start_event`)
  - belome3 brooch patch: `randomizer/patches/asm/belome3_brooch.py`

## Assemblers
Run from repo root: `PYTHONPATH=src patchvenv/bin/python src/smrpgpatchbuilder/manage.py <cmd> -t [-b] [-r ROM]`
- `animationassembler` → battle_animation (PRIMARY)
- `packassembler` → packs/formations
- `battleassembler` → monster_ai
- `enemyattackassembler`, `spellassembler`, `enemyassembler` as needed

## Verification smoke test (no ROM)
`... animationassembler -t` → must print "successfully assembled battle animation data", exit 0, 88 txt files.

## Setup status — DONE 2026-06-08
- Replaced `battle_animation/{02,35,3A}` with `/home/pidge/smrpg-condensed/src` (condensed original-game battle anim).
- Recreated `battle_animation/__init__.py` (required for dotted-package import by assembler).
- Old broken battle_animation preserved → `/home/pidge/code/_preserved_original_battle_animation_broken_20260608`
- FIX applied: condensed `script_0x3ACF48.py` used standard names JINX1/2/3Enemy → remapped by monster_id
  to postgame `JINXEnemy2`(195)/`JINXEnemy3`(196)/`JINXEnemy4`(218).
- Baseline assembles cleanly (88 scripts, 0 unresolved names).
- Clean-state backup (restore point): `/home/pidge/code/disassembler_output_BACKUP_clean-start_20260608` (90M).

## Formation mapping (postgame `id` → randomizer). Members = postgame class names.
| pg id | postgame members | randomizer formation |
|---|---|---|
| 405 | PUNCHINELLOEnemy, BOBOMBEnemy4, BOBOMBEnemy2, BOBOMBEnemy5, BOBOMBEnemy3 | FORM0124 (Punchinello2 + 4 strong bobombs) |
| 406 | BOOSTEREnemy2, SNIFITEnemy×3, booster2Enemy | FORM0123 (Booster + 3 Snifit2 + booster dummy) |
| 404 | BUNDTEnemy, RASPBERRYEnemy, TORTEEnemy×2, CANDLEEnemy | FORM0137 (Bundt2 + Raspberry2 + 2 Torte2 + Candle) |
| 403 | BELOMEEnemy3, MARIOCLONESEnemy, TOADSTOOL3Enemy | FORM0055 (Belome3 + MarioClones + Toadstool3) |
| 402 | JOHNNYEnemy | FORM0216 (Johnny2) |
| 401 | JINXEnemy, TeamGaugeEnemy | FORM0217 (Jinx4 + TeamGauge) — **pg uses JINXEnemy(78), rand uses JINXEnemy4(218): RECONCILE** |
| 407 | CULEX3DEnemy, FIRECRYS3DEnemy×4 | FORM0096 (Culex3D + Fire/Water/Earth/Wind crys 3D) — **3D sprites may be 2D copies in postgame** |

NOTE: postgame formation auto-generated NAMES are misleading (id405 is named "...ONE_WIND_CRYSTAL" but is Punchinello). Trust `id` + members.

## Per-formation checklist
- [x] 405 Punchinello + 4 strong bobombs (FORM0124) — DONE+ASSEMBLES (no bank-35 needed; sprites are duplicates)
- [x] 406 Booster + 3 Snifit + dummy (FORM0123) — DONE+ASSEMBLES. Booster(247) RemoveTarget(SELF)->ALL_ALLIES_AND_SELF; dummy(132) body=rd127 (BE0037 rename + structural); Snifit(173) unchanged; BE0037 UNUSED->BOOSTER_WORKING (battle_event_names + AI + script_0x3A6000 event body+sprseq using command_0x3A7544). No formation change (no start event). Attacks/spells used: Engine023Spell (Booster); snifit attacks TBD in shared pass.
- [x] 404 Bundt + Raspberry + 2 Torte + Candle (FORM0137) — DONE+ASSEMBLES. AI: raspberry(119)+2 var lines; torte(124) tail expand + BE0047 rename (kept pg event 47); candle(254) replaced w/ rd254 remapping formation ids 137->404,286->298; bundt(105) no change (attacks same _index). Added BV7EE006_ATTACK_PHASE_COUNTER alias. Battle events: ev13<-rd BE0017 (bundt2_sprq/sprq2 + candle summon SPR0510, jmp to ev38), ev38<-rd BE0038 (PARTY_SIZE->BV7EE00A), ev47<-rd BE0029 (torte2 sprq w/ torte2_sub0-5). kept pg run_event_at_load=13. imports added to script_0x3A6000.
- KEY: pg ATKMATK5Attack1=rd ATKMATK5Attack (idx24); pg ATKMATK5Attack2=rd ATKMATKneg5Attack (idx55) — attack names differ but _index matches, so NO change needed when diff only shows attack-name swap. ALWAYS check _index before "fixing" an attack.
- [x] 403 Belome3 + Mario clones + Toadstool3 (FORM0055) — DONE+ASSEMBLES (all 3 assemblers green). With the CORRECT ids the 3 AIs need NO CHANGE:
    - pg BELOMEEnemy3(201) ≡ rd201 — identical except pg keeps an extra RunBattleDialog(181) (per caveat) and BE0099_UNKNOWN(pg)==BE0099_BELOME_3_SUMMONS_CLONES(rd) is the SAME event id 99 (const-name only).
    - pg MARIOCLONESEnemy(227) ≡ rd131 and pg TOADSTOOL3Enemy(39) ≡ rd129 — byte-identical except BE0083_SCREEN_FLASHES_WHITE(pg)==BE0083_BELOME_3_CLONES(rd), same event id 83.
    - The old "rd marioclones uses IfCurrentlyInFormationID(292)" worry was from the WRONG-id diff; real rd131/rd129 have no formation check. No _force_start_event (Belome3Fight prize has none), FORM0055 members/positions == pg 403 → NO formation change.
    REAL WORK was battle events (script_0x3A6000 + script_0x3ACF48):
    - event 59: already ≡ rd (pg `extracted_subr_e074fdb…` = RunSub(3A771E)+Jmp(3A7550), so pg 59 expands to rd's 59). No change.
    - event 83: pg vanilla body REPLACED with rd clone-tracking logic INLINE in 3A6000 (reads BV7EE000/009/00A-00D, writes 0x7EFC4C/4E/74, AMEM 0x69-0x6F, labels belome3clone_1..5, ends Jmp command_0x3A7550). Kept pg identifier be0083_screen_flashes_white_0x3A6D66.
    - event 99: REPOINTED to `Jmp(["belome_3_outsourced"])`. GOTCHA: pg event 99's old body DEFINED `extracted_subr_ff8fe1c2…` (UseSpriteQueue field_object=2 command_0x3AC9AA) which event 100/earthlink Jmps to — PRESERVED it; only dropped the event-99-unique RunSub(command_0x3A755E).
    - belome_3_outsourced (~62 cmds, rd script_0x3ACF48.py L1720-1780) appended to pg script_0x3ACF48.py + 3 shared subrs MISSING from pg condensed disasm: command_0x3A7729 (4-cmd sprite-wait), command_0x3A6A08 (RunSub 3A771E;Jmp 3A7550), command_0x3ADAD8 (6-cmd, sets BV7EE00E bit1). All their deps (3A7531/3A7544/3A771E/3A7550/3AD9BC/3ADA4A) already in pg.
    - Clone sprites written as NUMERIC ids 387/385/381/334/428 (pg const names are stale NOTHING/CRIPPO/HAMMER_BRO_INTRO, ids match rd MARIO/TOADSTOOL/BOWSER/GENO/MALLOW_CLONE_S). Clone enemies MARIOCLONESEnemy/TOADSTOOL3Enemy/BOWSERCOPYSEnemy/GENOCLONESEnemy/MALLOWCOPYSEnemy all exist in pg by the SAME class name (kept verbatim, no remap).
- [~] 402 Johnny (FORM0216) — AI+FORMATION DONE+ASSEMBLES. Added 2 hidden WATERCRYSTALEnemy(150) to formation 402; johnny AI(175) +CallTarget(MONSTER_2/3_CALL)+RunBattleEvent(BE0030_JOHNY_2)+SetUntargetable(MONSTER_2/3). Johnny same id 175 both. BE0030_JOHNY_2 const already existed in pg.
  - DONE 2026-06-08 (via event-21 alias — user's insight): johnny_2's opening (event 30) is structurally a near-copy of "Johnny challenges Mario" (event 21) — in rd, event 30 ≈ event 21 (identical apart from johnny_2-specific sprite variants command_0x3AC09F_/3AC148_ and disambiguated johnny_skip__p3 labels). pg ALREADY HAS a working condensed event 21 (uses command_0x3AC063 + command_0x3AAFE2 + extracted_subr_33b618…, all present). So instead of porting rd's missing sprite cascade, RETARGETED pg event 30's alias from the event-29 stub → event-21 block: `DefineObjectQueue(["be0021_johnny_challenges_mario_to_a_one_on_one_0x3A641A"], identifier="battle_event_0030_unused")` + `Jmp(["be0021_…0x3A641A"])`. Event 30 now plays the johnny-challenge choreography (party members repositioning). Assembles, 88 files.
    - APPROXIMATION (acceptable per user "mostly a copy"): event 30 is now IDENTICAL to event 21; the johnny_2-only sprite variants (3AC09F_/148_) are NOT reproduced (they don't exist in pg's condensed base). A fully faithful event 30 would still need re-disassembling the johnny sprite region (the 3AC1F1/3ABBC6/3AC148 files are condensed differently and their extracted_subrs are load-bearing for 3ACF48/3ACCB1/3AC795/3AC7CF — can't be wholesale-replaced). The alias is the clean, faithful-enough realization.
- [~] 401 Jinx4 + TeamGauge (FORM0217) — CORE DONE+ASSEMBLES. pg JINXEnemy(78)+TeamGauge(186)=rd JINXEnemy4(180)+TeamGauge(97). Set formation run_event_at_load=39 + ported BE0039 (set 7EE00B=PARTY_SIZE) into pg event 39. jinx AI(78) RunObjectSequence(15)->14 (x3). TeamGauge(186) identical.
  - CORRECTION (earlier note was wrong): BE0012 is NOT dialogue — its body is just `UseSpriteQueue(field_object=0, command_0x3AB98A)` (booster-fight VISUAL). Battle events contain ZERO RunBattleDialog (all dialogue is in monster_ai). Jinx's real dialogue is RunBattleDialog(80) in the AI (untouched). So nothing was at stake in the BE0012-vs-BE0062 choice.
  - DONE 2026-06-08: jinx_4 special animation PORTED. jinx_4_outsourced (rd script_0x3ACF48.py L1892-2056, the jinx4 logic+sprite-seqs+TeamGauge queues; EXCLUDED the trailing solo_fire/water/earth/wind_sq blocks L2058-2081 which belong to event 76, not jinx) appended to pg script_0x3ACF48.py — self-contained (only command_0x3A7531/3A7544/3A7550/3A755E/3A771E, all in pg; effects EF0059/EF0082, sounds S0003/0006/0017/0110/0139 all in pg). WIRING: BE0012 is referenced ONLY by jinx(78), so repurposed pg event 12's body → `Jmp(["jinx_4_outsourced"])` (no AI change, AXEMRANGERS' BE0062 untouched, no dialogue lost). Jinx now plays the crystal/electric-bolt special animation.
- [x] 407 Culex3D + 4 crystals (FORM0096) — DONE+ASSEMBLES (all 3 assemblers green). CULEX3D=174 in both. Crystal monster_ids DIFFER: pg FIRE/WATER/EARTH/WIND = 129/130/131/242, rd = 183/185/203/242 (only Wind 242 matches); class names match so AIs port by pg id (compare pg129↔rd183, pg130↔rd185, pg131↔rd203, pg242↔rd242). 3D sprites SPR0749_WATER_FIRE_CRYSTAL_3D(749)/SPR0750_WIND_EARTH_CRYSTAL_3D(750) EXIST in pg (NOT 2D copies) — used directly by name.
    - Culex AI(174): only real change = Attack(DUMMYAttack17 _index=124) → Attack(Attack11 _index=11) ×2 (matches rd; verified _index). Kept pg's extra RunBattleDialog(128). pg's `BV7EE005_ATTACK_PHASE_COUNTER` == rd's `BV7EE006_ATTACK_PHASE_COUNTER` (BOTH = 0x7EE006; the pg "005" name is a misnomer) → NO change needed. BE0077 same id.
    - Crystal AIs(129/130/131/242): main body identical to rd; ported rd's counter-command tail only (adds `IfTargetAlive(MONSTER_1_SET)` guard before the force attack + a 2nd HP-below/IfTargetKOed death-handling pass). Per-crystal force attack kept (Vigor/Magic/Valor/Speed). All RunBattleDialog (145/146/147) preserved.
    - EVENT 77 (the crystal summon): pg had NO own block — root-queue index 77 was ALIASED to event 28 ("beat tentacles"), so the shipped condensed pg Culex fight ran the wrong event. Added a real block identifier="battle_event_0077_culex_3d" (rd BE0077_CULEX_3D body: 4× UseSpriteQueue field_object=1-4 → culex_subroutine_1-4, each RemoveObject + SetAMEM32ToXYZCoords + NewSpriteAtCoords(SPR0749/0750) + SummonMonster(FIRE/WATER/EARTH/WINDCRYS3DEnemy, position=1) + command_0x3A7544 + ReturnSpriteQueue) INLINE in 3A6000 between events 76 & 78, and REPOINTED root index 77 (unique anchor "…0076…","…0028…","…0078…" → middle → "battle_event_0077_culex_3d"). All deps (command_0x3A7531/3A7544/3A7550) already in pg; self-contained.
    - Event 74 (BE0074_CULEX_SUMMONS_CRYSTALS): LEFT ALONE — used by monster 255 (not in this formation); the culex fight summons via event 77.
    - FORMATION 407: members = 4× FIRECRYS3D placeholders (== rd Culex3DBossFight prize `_members`; event 77's SummonMonster sets each slot's real element by field_object, so placeholders are fine). RESOLVED 2026-06-08 (user): REMOVED run_event_at_load=77 — the crystal summon is correctly AI-driven (culex AI's `RunBattleEvent(BE0077)` on turn 1), matching rd (whose prize comments out `_force_start_event`). Formation 407 now has no load event.

## DIALOG SWEEP (2026-06-08) — item 2, RESOLVED to high confidence (full byte-exact ROM compare still needs disassembly):
- monster_ai dialogs: edited AIs (136,126,247,132,119,124,254,175,78 + 407's 174,129,130,131,242) vs clean backup — NO RunBattleDialog dropped (403 changed NO monster_ai, belome AI 201 untouched keeps RunBattleDialog(181); 407 culex 174 keeps 128/139/140/141/142/143/148, crystals keep 145/146/147; jinx 78 keeps RunBattleDialog(80)). The bosses' STORY DIALOGUE all lives here and is intact.
- battle-event text: `RunBattleDialog` is a MONSTER-SCRIPT command — battle events (bank 3A) CANNOT contain it (0 occurrences anywhere in pg battle_animation). Battle events show text only via `DisplayMessage`(op 0x7A)/`DisplayBonusMessage`(0x96)/`DisplayCantRunDialog`(0xD9). Every event I overwrote/added (403's 83/99+belome_3_outsourced, 407's 77, jinx's 12+jinx_4_outsourced) has ZERO of these in BOTH the pg-condensed original AND rd. Spot-check of the unheadered postgame .smc at the vanilla event offsets (0x3A6D66/0x3A7022/0x3A632B/0x3A65C4 — confirmed correct: each starts `10 31 75` = RunSubroutine command_0x3A7531) shows no 0x7A/0x96 opcodes either. → No battle text dropped.
- RESIDUAL (low risk, needs ROM disassembly — out of this session's no-disasm scope): the postgame author's REAL custom events may be RELOCATED in free ROM (not at vanilla offsets), so a byte-exact compare requires tracing the postgame ROM's run_event pointers via asm-trace/bsnes. Do separately if paranoid; the boss dialogue (AI-side) is already confirmed intact.

## SESSION SUMMARY (2026-06-08): DONE+ASSEMBLE (all 3 assemblers green): ALL 7 FORMATIONS FULL (405,406,404,403,407) + 401 jinx_4 animation ported + 402 johnny opening now animated (event-30 aliased to event-21 "johnny challenges Mario", per user's insight — no longer stubbed). BOTH previously-stubbed animations now resolved. Completed this session: formations 403 & 407, jinx_4 animation, johnny ev30 opening (alias). Backup restore: /home/pidge/code/disassembler_output_BACKUP_clean-start_20260608. REMAINING TODO: shared attack/spell/weapon-anim pass (item 3 — blocked by condensed bank-35 web, see Cross-cutting); full byte-exact ROM dialog compare (item 2 — needs disassembly; AI dialogs already confirmed intact). RESOLVED this session: 407 run_event_at_load removed (AI-driven summon); johnny ev30 opening now animated via event-21 alias; belome3_brooch built into the patch.

## COMBINED PATCH (built 2026-06-08) — base = Postgame Additions.smc
Builder: `build_postgame_patch.py` (repo root; `PYTHONPATH=src patchvenv/bin/python build_postgame_patch.py "<rom>" <out_dir>`). Output in `src/assembler_output/combined/`:
- `Postgame Additions + boss fights.smc` (patched ROM) + `postgame_boss_fights.bps` (bps verified: source/target/patch CRC32 all match; sizes equal 4MB).
Composition (~46292 bytes, 1065 regions, NO overlaps): anim_3A 32345 (ALL of bank 3A — see CRITICAL LESSON), monster_ai 9667 (full reassembly; large delta = pointer-table REPACKING, behaviour-preserving), packs 3854 (full reassembly), belome3_brooch 411, item73 15. Banks 35/02 (weapon/attack anims) LEFT as postgame's so custom weapons stay intact. Also emits per-region .bin files (bank 3A + monster_ai) to combined/bin/ for hex-editor clobbering.
**CRITICAL LESSON (fixed 2026-06-09):** battle events must be a FULL NUCLEAR replacement of bank 3A — NOT surgical. The condensed disassembly is a self-consistent LAYOUT that only works when the whole bank is present. Overlaying just the 2 edited blocks (3A6000+3ACF48) left dangling cross-refs into non-overlaid 3A files: e.g. event 59 → command_0x3AD902 → Jmp 0x3AB3D2, where the postgame's untouched byte was 0xBF ("data too short") instead of the condensed 0x44 0x60. Overlaying ALL of bank 3A makes every intra-bank ref resolve. (monster_ai/packs are the postgame's OWN disassembly so full overlay = postgame data + edits; bank 3A is condensed so it must be all-or-nothing.) Watch for bank 3A→35/02 refs if new issues surface.

## Shared static animation port (one-time; track attacks/spells/weapons used per fight)
- 405 uses attacks/spells: ATKDEF100, Elegy, SandStorm, FlameStone, Attack1, Grinder (Punchinello); ATKDEF100, BOBOMBSUPER (bobombs). Determine which are custom (need anim port) vs vanilla (already present) in the shared pass.

## Cross-cutting tasks (item 3 — ASSESSED 2026-06-08: NOT tractable in the current condensed-base / no-disassembly approach)
SCOPE FINDING: bank 35 (attack/spell/weapon anims) = 42 files, 40/41 DIFFER pg-vs-rd — NOT because of custom content but because pg's condensed base restructured them all (shared `extracted_subr_*` web across 35 + 3ACF48/3ACCB1/3AC795/3AC7CF). So a file diff can't isolate "custom", and porting rd anims in = same intractability as johnny ev30 (would break already-ported fights; needs un-condensing = violates no-ROM-disassembly rule).
- [~] Custom enemy attack/spell animations — EFFECTIVELY NONE NEEDED: the 7 bosses use VANILLA attacks (Meteor=94, Attack1, Vigor/Magic/Valor/SpeedForce, vanilla spells…) whose animations already exist in pg's vanilla-condensed base. No custom enemy-attack/spell anim port required.
- [ ] 3 weapons (Wonder Chomp / Stella 023 / Sage Stick) + per-character attack wrappers + Weapon Timed-Hit Sounds — BLOCKED: these live in the bank-35 character-attack animation system, entangled in the condensed `extracted_subr` web (johnny-style). Tractable only by re-disassembling bank 35 properly (out of scope here). Items exist in pg (Stella023Item/SageStickItem/WonderChompItem in items/items.py).
- [x] belome3_brooch — DONE 2026-06-08 (included in the combined patch). It's a 579-line ASM ENGINE-HOOK patch (rd `randomizer/patches/asm/belome3_brooch.py`); `get_patch(infuse_spell_elements=False)` returns `{rom_offset: bytes}` (4 JSL hooks @0x02972E/0x02C55E/0x02C9FE/0x02CA73 + 4 free-ROM routines @0x0FF7B0+, 411 bytes total). AUDIT vs Postgame Additions.smc: free-ROM 0x0FF7B0..0x100000 confirmed all-zero (no collision); all 4 hook sites hold the vanilla bytes the patch displaces; Belome3=201 & BowserCopyS=125 both match (immunity half CORRECT); ranges disjoint from anim/AI/pack changes. RESOLVED (user opt #2): item 73 REPURPOSED into the Enduring Brooch. In items/items.py, SpareItem2 (class name kept for ref-safety: item list + __init__ + overworld event 3012 AddToInventory) changed Armor→Accessory + _item_name="EnduringBrch", _prefix=RING, _price=2, _prevent_ko=True (mirrors rd EnduringBroochItem). Patch overlays item 73's render() (3 fixed regions: stats 0x3A066F, price 0x3A4184, name 0x3A4B36) — functional accessory + name. CAVEAT: the flavor DESCRIPTION (" Prevents KOs") is NOT applied — it needs the full ALL_ITEMS.render() which is blocked by PRE-EXISTING postgame item-data bugs (curly-apostrophe ’ in B'tub Ring/Lamb's Lure names [fixed, byte-null: ROM has 0x7E either way], AND "weapon IDs can only be 0-40" — likely the custom postgame weapons). Belome-3 spell-immunity half works as-is.

## Per-formation procedure (from user)
1. Compare battle events between sources (by content incl. subroutines/branches/sprite queues, not just id).
   Missing in postgame → add new battle event (new entry in script_0x3A6000 root queue) + set formation `run_event_at_load`.
   Event exists but differs → overwrite postgame event body with randomizer's (keep postgame's event id).
   Also check `prizes.py` `_force_start_event` for the formation's intended start event.
2. Compare monster AI of each member (ids differ between sources; randomizer = source of truth).
   AI references → battle events (overwrite postgame body w/ randomizer content, keep pg id),
   attacks & spells (port animation code, use postgame ids), the 3 special weapons.
3. Port attack wrappers, weapon timed-hit sounds, shared subroutines.
4. Choose insertion script file by matching free space (expected_size − current code length).

## ID-mapping notes (append as discovered)
- JINX anim summon: JINX1Enemy(195)→pg JINXEnemy2; JINX2Enemy(196)→pg JINXEnemy3; JINX3Enemy(218)→pg JINXEnemy4

### Formation 405 (Punchinello + 4 strong bobombs) — ANALYSIS COMPLETE, awaiting approval
Position→slot→enemy map (positions identical both sources):
- slot0 (188,116): pg PUNCHINELLOEnemy(136) = rd PUNCHINELLO2Enemy(136)  [same id]
- slot1/MONSTER_2 (145,103): pg BOBOMBEnemy4(127) = rd STRONGBOBOMB3(160); var BV7EE001
- slot2/MONSTER_3 (150,129): pg BOBOMBEnemy2(115) = rd STRONGBOBOMB1(141); var BV7EE002
- slot3/MONSTER_4 (182,142): pg BOBOMBEnemy5(185) = rd STRONGBOBOMB4(173); var BV7EE003
- slot4/MONSTER_5 (223,142): pg BOBOMBEnemy3(126) = rd STRONGBOBOMB2(159); var BV7EE004→**BV7EE008** (scratch-var fix)
Start event: NONE (no _force_start_event; no run_event_at_load) → no formation change.
AI edits: script_136 BV7EE004→008 (x2, MONSTER_5 check/clear); script_126 BV7EE004→008 (x2 SetVarBits). Others unchanged.
Battle event 68: pg "unused" stub → port randomizer's `punchinello_2_outsourced` (rd script_0x3ACF48.py L1809-1890, ~83 lines) + set BE68 to Jmp to it.
  - enemy remap in block: STRONGBOBOMB3→BOBOMBEnemy4, 1→2, 4→5, 2→3
  - sprite remap NEEDED (custom): rd SPR0397_BOBOMB_S_1 / 0415_S_2 / 0416_S_3 / 0429_S_4 → postgame ids = ??? (ASK USER)
  - direction vars (rd battle_animation_variable_names): BOBOMB_S_160_DIRECTION=0x7FFFC0, _141_=0x7FFFD0, _173_=0x7FFFE0, _159_=0x7FFFF0 (add to pg vars)
  - needs import of battle_variable_names (BV7EE00A-D) in target script; subroutines 3A7531/755E/771E/7550 already exist in pg
Attacks/spells used: ATKDEF100, Elegy, SandStorm, FlameStone, Attack1, Grinder, BOBOMBSUPER (all vanilla — verify anim parity, likely no port).
SPRITE RULE (user): monster battle sprite id = monster_id + 256. So pg bobomb sprites: 115→371, 126→382, 127→383, 185→441 (names there are stale: GUNYOLK/MASTABLASTA/PILE_DRIVER/THWOMP — use the id).
Object queue (script_0x350202): pg & rd BOTH point these monster slots to monster_sprite_behaviour_0_no_movement_for_escape — NO rewiring.
Bank-35 port NEEDED: rd script_0x358BEC.py has bobomb_s object-sequences (10/11/12 for set 0-1-2-3, per bobomb 141/159/160/173) reached by AI RunObjectSequence(11/3); they read BOBOMB_S_*_DIRECTION. Not in pg condensed → transplant into pg script_0x358BEC (verify command_0x3505D5 exists in pg).
Summon (punchinello_2_outsourced) is self-contained: only calls command_0x3A7550/7531/755E/771E (all exist in pg) + own internal sprq labels.
405 FULL EDIT SET:
  - monster_ai/script_136: BV7EE004→BV7EE008 x2; script_126: BV7EE004→BV7EE008 x2.
  - bank3A: insert punchinello_2_outsourced (remap STRONGBOBOMB3/1/4/2→BOBOMBEnemy4/2/5/3, sprites→383/371/441/382, dir vars); repoint battle_event_0068 → Jmp(["punchinello_2_outsourced"]).
  - bank35: transplant bobomb_s object-sequences into script_0x358BEC.
  - variables: add BOBOMB_S_{160,141,173,159}_DIRECTION = 0x7FFFC0/D0/E0/F0 (+ import battle_variable_names where needed).
  - formation: NO change.
405 STATUS (2026-06-08):
  DONE+ASSEMBLES: script_136/126 BV fix; battle_event_names BE0068 rename; punchinello_2_outsourced inserted into pg script_0x3ACF48.py (sprites 383/371/441/382, BOBOMBEnemy4/2/5/3); BE68 repointed; battle_animation_variable_names.py created (copied from rd); imports added to script_0x3ACF48. animationassembler -t green (88), battleassembler -t green.
  PENDING bank-35 obj sequences (bobomb hit-reaction anims, RunObjectSequence 10/11/12/13):
    - rd dispatch: script_0x350737.py L85-88 (JmpIfAMEM16BitEqualsConst 0x60 ==10/11/12/13 -> bobomb_obj_seq_N) woven into shared behaviour code.
    - rd seq defs: bobomb_obj_seq_13 in script_0x350737.py L247; bobomb_obj_seq_10/11/12 in script_0x358BEC.py ~L4135-4198 (object_sequence_1X_for_set_0-1-2-3_bobomb_s_*).
    - RunObjectSequence(3) already works (std seq command_0x350796). Only 10-13 are custom.
    - behaviour table = monster_sprite_behaviour_0_no_movement_for_escape (script_0x35058A.py L17, 6-seq queue) — SHARED, so dispatch modifies shared code. Risk: verify doesn't break other monsters.
    - Fight FUNCTIONS without this (bobombs summon+attack+die); this is hit-reaction animation polish.

### Sprite-ID strategy (general)
Vanilla sprite ids match across sources (e.g. SPR0474_JINX_RD_TIME both). Only NEW/custom sprites differ
(strong bobombs, culex/crystal 3D, the 3 weapons). Need pg ids for each custom sprite as encountered.

## Gotchas
- Randomizer anim scripts import `variables.battle_animation_variable_names` + `battle_variable_names`;
  postgame condensed scripts import a different variable set. Watch import differences when porting code over.
- Strong bobombs: 4 near-identical AI; randomizer changed the target-state variable for ≥1 (one pg bobomb used a scratch var).
- Culex/crystal 3D sprites in randomizer may just be 2D-sprite copies in postgame (e.g. sprite 511 for culex).
- BLOCK CAPACITY / FREE SPACE (how outsourced routines fit): each `AnimationScriptBlock(expected_size=N, …)` is a FIXED ROM region. `render()` (datatypes/battle_animation_scripts/types.py L147) pads the assembled code up to N with `ReturnSubroutine()` = opcode **0x11**; it RAISES if code > N. So a block always renders to exactly N bytes and the txt output is padded — "N/N used" does NOT mean full. To get TRUE headroom: run `animationassembler -t`, then count the TRAILING run of `11` tokens in `src/assembler_output/battle_animations/txt/write_to_0x<ADDR>.txt` (that run = free padding). Appending a new outsourced routine just CONSUMES padding inside the same region (no range expansion, no patch-audit needed) — this is why punchinello_2 & belome_3 fit. As of 403: 3A6000 ~655 bytes free, 3ACF48 (the scratch file for outsourced summon routines) ~2662 bytes free. Cross-FILE Jmp works (event in 3A6000 → label in 3ACF48), so put new summon routines + their missing shared subrs in 3ACF48.
- pg CONDENSED disasm ≠ rd disasm structurally even for the SAME vanilla region/address. The condense pass de-duplicated shared sprite-wait subrs into parameterized loops + `extracted_subr_<hash>` blocks, so individual rd entry-point labels (e.g. command_0x3A7729/3A6A08/3ADAD8, or the per-bit waits in script_0x3A7702) may NOT exist in pg even though the bytes do. When a ported routine calls such a label: check `grep -rn 'identifier="<label>"' .../3A/contents/`; if MISSING, port the tiny rd subroutine (they're self-contained, a few cmds) into the scratch block. Also: a pg `extracted_subr_<hash>` defined INSIDE an event body may be Jmp'd to by ANOTHER event — before overwriting an event body, grep the hash to preserve any shared block (see 403 event 99 → earthlink/event 100).
- ENEMY/SPRITE name reconciliation for ports: clone/summon enemies often share the SAME class name across sources even when monster_id differs (MARIOCLONESEnemy, TOADSTOOL3Enemy, BOWSERCOPYS/GENOCLONES/MALLOWCOPYS all exist in pg) → keep the class name, no remap. Custom sprite CONST names are stale in pg (SPR0385_NOTHING vs rd SPR0385_TOADSTOOL_CLONE_S) but the numeric id matches → write sprite_id as the NUMBER (387/385/381/334/428 for the clones).

## SESSION 3 (2026-06-09): RE-PORT ONTO CORRECTED CONDENSED BASE — DONE; overworld + disasm-audit IN PROGRESS

### Core boss re-port: COMPLETE + VALIDATED
- Corrected condensed base PRODUCED via sandbox condenser at `/home/pidge/code/_condense_work/`
  (copy of smrpg-condensed-audit/tools with hardcoded `/home/pidge/smrpg-condensed/` paths sed-rewritten to the work dir;
  `run_condense.py` PATCHED to NOT shrink expected_size — keeps each block at full slot size for the full-bank nuclear overlay).
  FRESH input = `/home/pidge/smrpg-condensed/src` (the FULL vanilla disasm; confirmed FULL, not condensed: condenser emits `cond_N` labels, that tree has zero).
  Gates PASS: verify_final (inline-expansion == fresh F), dead-code scan = 0 (vs 310 buggy), gate validated (forced Jmp->RunSub on cond_371 caught). 9496 B freed.
- Integrated into LIVE `src/disassembler_output/battle_animation/{02,35,3A}` (imports converted `from disassembler_output.` -> `from ....`). STOCK `animationassembler -t` green = 89 scripts (88 + new 0x3A5620 block).
- Boss re-port (10 event bodies validated command/arg-identical to backup): 3A6000 root index 77 -> battle_event_0077_culex_3d; events 12(jinx_4),13(bundt2),30(alias->ev21),37(booster),38,39,47(torte2),68(punch),83(belome3clone),99(belome_3). NEW block `3A/contents/script_0x3A5620.py` (expected_size=1259, slot 0x3A5620..0x3A6000 = 2528 B, verified all-zero in vanilla+postgame) holds culex ev77 body + punchinello_2/belome_3/jinx_4 outsourced. The 3 formerly-"missing" shared subrs (command_0x3A7729/3A6A08/3ADAD8) ALREADY EXIST in the corrected base -> dropped from the append. command_0x3AD902/event-59 bug GONE (no Jmp 0x3AB3D2; equivalence-verified).
- Per-block fit: 3A6000 rendered 4077/4189 (112 free); 0x3A5620 1259 exact; 3ACF48 6800/7676 (pure condensed vanilla, untouched).
- COMBINED PATCH (build_postgame_patch.py vs "Postgame Additions.smc" base): `src/assembler_output/combined/postgame_boss_fights.bps` (44385 B: anim_3A 30438, monster_ai 9667, packs 3854, belome3_brooch 411, item73 15). STEP-1 vanilla base BPS: `/home/pidge/code/_condense_work/assembler_output/bps/smrpg-condensed-base.bps` (condensed vanilla vs /mnt/d/smrpg.sfc, in-scope battle-anim only).
- BACKUPS: `_battle_animation_BACKUP_pre_rebase_20260609_084202`; `_disassembler_output_BACKUP_pre_disasm_fix_20260609_112324` (overworld_scripts+packets pre-conversion).

### OVERWORLD inclusion: ~99% (one blocker left) — user wants it in the combined patch
- Root cause (user-confirmed): datatype command/Packet classes were renamed/added but the disassemblers were never updated (git history). disassembler_output's overworld is legacy-format.
- FIXED in disassembler_output (faithful, render-verified == original bytes): reserved action opcodes 0x20->A_ToggleSubroutineSlots, 0x24->A_SetSubroutineXTargets, event 0xFD 0x8E->DarkenLayersExceptPaletteRows (466 instances). packets.py: shadow->show_shadow + unknown_bits/unknown_bytes->b0/vram_size/sprite_priority/layer_priority/b2b2/b2b3/b2b4/b2/b4 (byte2 bits0-1 dropped = unused by current Packet; irrelevant for event-script refs which use packet_id). Converters: `/tmp/convert_overworld.py`, `/tmp/convert_packets.py`.
- REMAINING BLOCKER: 7 stale ITEM-constant names referenced in event scripts but absent from items.py (NameError): MuteBombItem(3), BaneBombItem(3), BombItem(2), DebugBombItem(2), DoomBombItem(1), FearBombItem(1), SleepBombItem(1). items.py has SleepyBomb/Fire/Ice/Bambino/Fright/SCrowBomb. Need old->current mapping (by item id / git). Likely vanilla status-bomb items renamed.
- OVERWORLD HAS REAL EDITS to preserve (user): event scripts 3500, 3503; action scripts 1018, 1019, 1021. (In-place conversion preserves them; do NOT overwrite via re-disasm.)
- Once items resolved: `eventassembler -t` green, then add overworld render (events.banks + actionqueues.actions, at bank.pointer_table_start) to build_postgame_patch.py and rebuild.

### DISASSEMBLER UPDATE + AUDIT: PENDING (user request, for future use)
- Update `management/commands/legacy/eventdisassembler.py` (overworld event+action; emit A_ToggleSubroutineSlots/A_SetSubroutineXTargets/DarkenLayersExceptPaletteRows for 0x20/0x24/0xFD8E + any other classed opcodes) and `packetdisassembler.py` (emit current Packet API b0/vram_size/... + show_shadow) so future disassembly is current-format.
- AUDIT all ~40 disassemblers for the same drift (stale class names, A_UnknownCommand/UnknownCommand for now-classed opcodes). VALIDATE by re-disassembling to a NEW/scratch folder (NEVER overwrite disassembler_output) and round-tripping vs the ROM.

### SESSION 3 UPDATE — overworld cascade is OPEN-ENDED; recommend disassembler-fix + re-disasm path
- After fixing commands(0x20/0x24/0xFD8E)+packets+items, eventassembler hits MORE stale-constant drift:
  next is `SUPER_MARIO` (DisplayIntroTitleText text enum) in event script_2357, and likely many more
  (legacy/eventdisassembler.py is OLD; many enums/constants renamed since). Grinding the existing
  output is whack-a-mole.
- DECISION: the CLEAN path for the overworld is the user's disassembler-update ask: fix
  legacy/eventdisassembler.py + packetdisassembler.py (+ enum/constant names) to emit current
  symbols, RE-DISASSEMBLE overworld+packets to a NEW folder (round-trip vs ROM), then PORT the 5
  edits (event 3500/3503, action 1018/1019/1021). Do in a fresh context (sizeable).
- In-place conversions already applied to disassembler_output (faithful, render-verified) are kept
  as progress: overworld opcodes 0x20/0x24/0xFD8E, packets API, items/__init__.py debug-bomb stubs
  (MuteBomb/BaneBomb/Bomb/DebugBomb/DoomBomb/FearBomb/SleepBomb = SleepyBombItem; unused). Original
  preserved at _disassembler_output_BACKUP_pre_disasm_fix_20260609_112324.
- CORE boss deliverable is unaffected (build_postgame_patch imports items.items/monster_ai/packs/
  battle_animation.3A/belome3_brooch — none touched by the overworld/packets/__init__ edits).
