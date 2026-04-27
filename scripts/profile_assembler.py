"""Diagnostic: run the assembler with timing prints inserted at key
points in the render pipeline so we can see where it spends time.
"""
import importlib
import sys
import time
from copy import deepcopy

t0 = time.monotonic()
def log(msg: str) -> None:
    print(f"[{time.monotonic()-t0:7.1f}s] {msg}", flush=True)

ROM = sys.argv[1]
log("Reading ROM")
original = bytearray(open(ROM, "rb").read())
rom = deepcopy(original)

log("Importing sprites module")
module = importlib.import_module("disassembler_output.sprites.sprites")
bank = module.sprites
log(f"Imported. Sprite count: {len(bank.sprites)}")

# Monkey-patch progress prints into the SpriteCollection methods.
from smrpgpatchbuilder.datatypes.graphics import classes as gx

orig_assemble = gx.SpriteCollection.assemble_from_tables
orig_assemble_ = gx.SpriteCollection.assemble_from_tables_

def patched_assemble(self, sprites, insert_whitespace=False, shared_image_groups=None):
    log(f"assemble_from_tables: start ({len(sprites)} sprites)")
    return orig_assemble(self, sprites, insert_whitespace, shared_image_groups)

def patched_assemble_(self, sprites, images, animations, output_tile_ranges=[]):
    log(f"assemble_from_tables_: start ({len(sprites)} sprites, {len(images)} images, {len(animations)} animations)")
    out = orig_assemble_(self, sprites, images, animations, output_tile_ranges)
    log("assemble_from_tables_: done")
    return out

gx.SpriteCollection.assemble_from_tables = patched_assemble
gx.SpriteCollection.assemble_from_tables_ = patched_assemble_

# Insert finer-grain prints by wrapping helpers
orig_find_clones = gx.find_clones
find_clones_calls = [0]
def patched_find_clones(*a, **kw):
    find_clones_calls[0] += 1
    if find_clones_calls[0] % 50 == 0:
        log(f"find_clones called {find_clones_calls[0]} times")
    return orig_find_clones(*a, **kw)
gx.find_clones = patched_find_clones

orig_is_same = gx.is_same_animation
is_same_calls = [0]
def patched_is_same(*a, **kw):
    is_same_calls[0] += 1
    if is_same_calls[0] % 100000 == 0:
        log(f"is_same_animation called {is_same_calls[0]} times")
    return orig_is_same(*a, **kw)
gx.is_same_animation = patched_is_same

log("Starting render()")
output = bank.render(False)
log("render() returned")
log(f"is_same_animation total calls: {is_same_calls[0]}, find_clones: {find_clones_calls[0]}")
