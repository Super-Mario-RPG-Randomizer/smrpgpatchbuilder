"""Assemble every disassembler_output module into ONE bps patch.

comboassembler runs each assembler separately, so it emits one bps per data
type. This applies every render() to a single ROM copy and diffs once.
"""

import importlib
import os
from copy import deepcopy
from datetime import datetime

from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress
from django.core.management.base import BaseCommand

OUT_DIR = "./src/assembler_output/full"


def _dict_source(module_path, attr):
    """render() -> dict[int, bytearray]"""

    def get(options):
        collection = getattr(importlib.import_module(module_path), attr)
        return list(collection.render().items())

    return get


def _pairs_source(module_path, attr, *render_args):
    """render() -> list[(start, bytes)]"""

    def get(options):
        bank = getattr(importlib.import_module(module_path), attr)
        return list(bank.render(*render_args))

    return get


def _enemies(options):
    collection = importlib.import_module("disassembler_output.enemies.enemies").ALL_ENEMIES
    return list(collection.render(psychopath=not options.get("no_psychopath")).items())


def _monster_ai(options):
    """render() -> (bytes, bytes) for two fixed addresses"""
    module = importlib.import_module("disassembler_output.monster_ai.monster_scripts")
    output = module.monster_scripts.render()
    return [(0x3930AA, output[0]), (0x39F400, output[1])]


def _event_scripts(options):
    module = importlib.import_module("disassembler_output.overworld_scripts.event.events")
    return [(bank.pointer_table_start, bank.render()) for bank in module.events.banks]


def _action_queues(options):
    module = importlib.import_module("disassembler_output.overworld_scripts.animation.actionqueues")
    return [(module.actions.pointer_table_start, module.actions.render())]


SOURCES = [
    ("items", _dict_source("disassembler_output.items.items", "ALL_ITEMS")),
    ("allies", _dict_source("disassembler_output.allies.allies", "ally_collection")),
    ("enemies", _enemies),
    ("enemy_attacks", _dict_source("disassembler_output.enemy_attacks.attacks", "collection")),
    ("spells", _dict_source("disassembler_output.spells.spells", "ALL_SPELLS")),
    ("packets", _dict_source("disassembler_output.packets.packets", "ALL_PACKETS")),
    ("battle_dialogs", _dict_source("disassembler_output.battle_dialogs.battle_dialogs", "collection")),
    ("dialogs", _dict_source("disassembler_output.dialogs.dialogs", "data")),
    ("shops", _dict_source("disassembler_output.shops.shops", "shop_collection")),
    ("packs", _dict_source("disassembler_output.packs.pack_collection", "pack_collection")),
    ("rooms", _dict_source("disassembler_output.rooms.rooms", "room_collection")),
    ("world_map_locations", _dict_source("disassembler_output.world_map_locations.world_map_locations", "world_map_location_collection")),
    ("event_palettes", _dict_source("disassembler_output.event_palettes.event_palettes", "ALL_EVENT_PALETTES")),
    ("sprite_palettes", _dict_source("disassembler_output.sprite_palettes.sprite_palettes", "ALL_SPRITE_PALETTES")),
    ("monster_ai", _monster_ai),
    ("battle_animation_3A", _pairs_source("disassembler_output.battle_animation.3A.export", "bank")),
    ("battle_animation_35", _pairs_source("disassembler_output.battle_animation.35.export", "bank")),
    ("battle_animation_02", _pairs_source("disassembler_output.battle_animation.02.export", "bank")),
    ("sprites", _pairs_source("disassembler_output.sprites.sprites", "sprites", False)),
    ("event_scripts", _event_scripts),
    ("action_queues", _action_queues),
]


class Command(BaseCommand):
    help = "assemble all disassembler_output data into a single bps patch"

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", required=True, help="path to the base mario rpg rom")
        parser.add_argument("-o", "--out", dest="out", help=f"output .bps path (default: {OUT_DIR}/)")
        parser.add_argument(
            "--partial",
            action="store_true",
            dest="partial",
            help="write the patch even if some data types failed to assemble",
        )
        parser.add_argument(
            "--only",
            dest="only",
            help="comma-separated subset of data types to assemble",
        )
        parser.add_argument(
            "--no-psychopath",
            action="store_true",
            dest="no_psychopath",
            help="leave psychopath messages alone (they render uncompressed, so a full vanilla round-trip doesn't fit).",
        )

    def handle(self, *args, **options):
        original_rom = bytearray(open(options["rom"], "rb").read())
        rom = deepcopy(original_rom)

        sources = SOURCES
        if options.get("only"):
            wanted = {s.strip() for s in options["only"].split(",")}
            unknown = wanted - {name for name, _ in SOURCES}
            if unknown:
                self.stderr.write(self.style.ERROR(f"unknown data types: {', '.join(sorted(unknown))}"))
                exit(1)
            sources = [(name, fn) for name, fn in SOURCES if name in wanted]

        owner = {}  # start address -> label, for collision reporting
        failures = []

        for label, fn in sources:
            try:
                blocks = fn(options)
            except Exception as e:  # noqa: BLE001 - report every failure, don't stop at the first
                failures.append((label, f"{type(e).__name__}: {e}"))
                self.stdout.write(self.style.ERROR(f"  x {label}: {type(e).__name__}: {e}"))
                continue

            total = 0
            for start, bytes_ in blocks:
                end = start + len(bytes_)
                if end > len(rom):
                    failures.append((label, f"change at {start:#X} exceeds file size (end = {end:#X})"))
                    break
                for prev_start, (prev_end, prev_label) in owner.items():
                    if prev_label != label and start < prev_end and prev_start < end:
                        self.stdout.write(
                            self.style.WARNING(
                                f"  ! {label} 0x{start:06X}-0x{end:06X} overlaps {prev_label} "
                                f"0x{prev_start:06X}-0x{prev_end:06X}; {label} wins"
                            )
                        )
                owner[start] = (end, label)
                rom[start:end] = bytes_
                total += len(bytes_)
            else:
                self.stdout.write(self.style.SUCCESS(f"  + {label}: {len(blocks)} blocks, {total} bytes"))

        if failures and not options["partial"]:
            self.stderr.write(self.style.ERROR("\nno patch written. failed data types:"))
            for label, err in failures:
                self.stderr.write(self.style.ERROR(f"  {label}: {err}"))
            self.stderr.write(self.style.ERROR("re-run with --partial to patch anyway."))
            exit(1)

        changed = sum(1 for a, b in zip(original_rom, rom) if a != b)
        out_path = options.get("out")
        if not out_path:
            os.makedirs(f"{OUT_DIR}/bps", exist_ok=True)
            out_path = f'{OUT_DIR}/bps/smrpg-{datetime.now().strftime("%Y%m%d%H%M%S")}.bps'
        else:
            os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)

        blocksize = (len(original_rom) + len(rom)) // 1000000 + 1
        iterable = diff_bytearrays(blocksize, bytes(original_rom), bytes(rom))
        with open(out_path, "wb") as f:
            write_bps(bps_progress(iterable), f)

        self.stdout.write(self.style.SUCCESS(f"\n{changed} bytes changed vs base rom"))
        if failures:
            self.stdout.write(self.style.WARNING(f"PARTIAL patch - {len(failures)} data types omitted"))
        self.stdout.write(self.style.SUCCESS(f"wrote {out_path}"))
