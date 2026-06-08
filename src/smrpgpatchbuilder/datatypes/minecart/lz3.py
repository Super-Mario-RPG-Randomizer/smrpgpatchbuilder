"""LC_LZ3 encoder — the compression format Super Mario RPG uses for its Mode7
graphics/tilemaps (the game's decompressor lives at ``$C0:F7B6`` and dispatches
on the *low nibble* of each command byte through a 16-entry table at
``$00:FBCC``).

Command grammar (a stream is a run of commands ending in a ``0xFF`` terminator;
in ROM each stored stream is additionally prefixed by one ``0x01`` byte that the
loader skips — callers add/strip that prefix, it is NOT part of the stream):

    byte C < 0xF0          -> copy (C + 1) literal bytes from the stream
    0xF1 N V               -> fill (N + 4) bytes with value V
    0xF8 N V               -> fill (N + 4) bytes V, V+1, V+2, ... (wrapping)
    0xFF                   -> end of stream
    0xF0 / 0xF2..0xFE      -> nibble / word / 2D-stride / back-reference fills
                             (used by vanilla data; this encoder never emits them)

This encoder emits four commands: literal copy, constant-fill (``0xF1``),
increasing-fill (``0xF8``) and the LZ back-reference (``0xFD``). That set
round-trips losslessly and compresses the highly repetitive minecart tilemaps
(flat track runs, the ascending "brick" background texture, and its repeating
horizontal period) within the game's fixed 0x8000 data window. The matching
:func:`decompress` understands exactly those commands, which is enough to verify
the encoder; the full 15-command decoder is not needed to *write* patches.

The encoder was validated against the game's own routine (a cycle-faithful
emulator of ``$C0:F7B6``): ``decompress(compress(x)) == x`` for random data and
for every vanilla minecart section.
"""

from collections import defaultdict
from typing import Dict, List, Tuple

_LITERAL_MAX = 240   # byte 0xEF -> copy 240 literal bytes
_FILL_MAX = 259      # 0xF1/0xF8 with N=255 -> 259 bytes
_FILL_MIN = 4        # fill commands always produce at least 4 bytes
_TERMINATOR = 0xFF
_CMD_CONST_FILL = 0xF1
_CMD_INC_FILL = 0xF8
_CMD_BACKREF = 0xFD

_BR_MIN = 0x14       # 0xFD length is operand + 0x14
_BR_MAX = 0x14 + 0xFF   # 275
_BR_MAX_DIST = 0x100    # 0xFD distance is operand + 1, so 1..256
_CHAIN_CAP = 64         # cap match candidates per key (keeps the matcher cheap)


def _flush_literals(out: bytearray, data: bytes, start: int, end: int) -> None:
    """Emit ``data[start:end]`` as one or more literal-copy commands."""
    j = start
    while j < end:
        chunk = min(_LITERAL_MAX, end - j)
        out.append(chunk - 1)            # 0x00..0xEF
        out.extend(data[j : j + chunk])
        j += chunk


def _best_backref(data: bytes, i: int, n: int,
                  chains: Dict[bytes, List[int]]) -> Tuple[int, int]:
    """Longest LZ match ending the search at ``i``: returns ``(length, dist)``
    with an *even* distance (so the game's 2-byte-word copy reproduces it
    exactly) and ``length`` in ``[_BR_MIN, _BR_MAX]``, or ``(0, 0)``."""
    if i + 2 >= n:
        return 0, 0
    candidates = chains.get(data[i : i + 3])
    if not candidates:
        return 0, 0
    floor = i - _BR_MAX_DIST
    max_len = min(_BR_MAX, n - i)
    best_len, best_dist = 0, 0
    for j in reversed(candidates):             # most recent (smallest dist) first
        if j < floor:
            break
        dist = i - j
        if dist % 2:                           # need even distance
            continue
        length = 0
        while length < max_len and data[i + length] == data[i - dist + length]:
            length += 1
        if length > best_len:
            best_len, best_dist = length, dist
            if length >= max_len:
                break
    return best_len, best_dist


def compress(data: bytes) -> bytes:
    """Encode ``data`` into an LC_LZ3 stream (terminated by ``0xFF``)."""
    out = bytearray()
    n = len(data)
    i = 0
    literal_start = 0
    chains: Dict[bytes, List[int]] = defaultdict(list)

    def remember(start: int, end: int) -> None:
        for j in range(start, end):
            if j + 2 < n:
                key = data[j : j + 3]
                lst = chains[key]
                lst.append(j)
                if len(lst) > _CHAIN_CAP:
                    del lst[0]

    while i < n:
        v = data[i]
        const_run = 1
        while i + const_run < n and data[i + const_run] == v:
            const_run += 1
        inc_run = 1
        while i + inc_run < n and data[i + inc_run] == ((v + inc_run) & 0xFF):
            inc_run += 1
        br_len, br_dist = _best_backref(data, i, n, chains)

        if br_len >= _BR_MIN and br_len >= const_run and br_len >= inc_run:
            _flush_literals(out, data, literal_start, i)
            out += bytes([_CMD_BACKREF, br_dist - 1, br_len - _BR_MIN])
            remember(i, i + br_len)
            i += br_len
            literal_start = i
        elif const_run >= _FILL_MIN and const_run >= inc_run:
            _flush_literals(out, data, literal_start, i)
            remaining = const_run
            while remaining >= _FILL_MIN:
                run = min(remaining, _FILL_MAX)
                out += bytes([_CMD_CONST_FILL, run - _FILL_MIN, v])
                remaining -= run
            covered = const_run - remaining
            remember(i, i + covered)
            i += covered
            literal_start = i
            for _ in range(remaining):         # 0..3 leftover -> literals
                remember(i, i + 1)
                i += 1
        elif inc_run >= _FILL_MIN:
            _flush_literals(out, data, literal_start, i)
            covered = 0
            while inc_run - covered >= _FILL_MIN:
                run = min(inc_run - covered, _FILL_MAX)
                out += bytes([_CMD_INC_FILL, run - _FILL_MIN, (v + covered) & 0xFF])
                covered += run
            remember(i, i + covered)
            i += covered
            literal_start = i
        else:
            remember(i, i + 1)
            i += 1                             # extend pending literal run

    _flush_literals(out, data, literal_start, n)
    out.append(_TERMINATOR)
    return bytes(out)


def decompress(stream: bytes, offset: int = 0) -> bytes:
    """Decode an LC_LZ3 stream produced by :func:`compress`.

    Handles the literal / constant-fill (``0xF1``) / increasing-fill (``0xF8``)
    commands this module emits. Raises on any other command — full vanilla data
    uses additional fill/back-reference commands that the encoder never produces.
    """
    out = bytearray()
    p = offset
    while p < len(stream):
        c = stream[p]
        p += 1
        if c == _TERMINATOR:
            break
        if c < 0xF0:                           # literal copy
            length = c + 1
            out += stream[p : p + length]
            p += length
        elif c == _CMD_CONST_FILL:
            length = stream[p] + _FILL_MIN
            value = stream[p + 1]
            p += 2
            out += bytes([value]) * length
        elif c == _CMD_INC_FILL:
            length = stream[p] + _FILL_MIN
            value = stream[p + 1]
            p += 2
            out += bytes([(value + k) & 0xFF for k in range(length)])
        elif c == _CMD_BACKREF:
            dist = stream[p] + 1
            length = stream[p + 1] + _BR_MIN
            p += 2
            src = len(out) - dist          # encoder only emits even dist, so the
            for k in range(length):        # game's 2-byte-word copy == byte copy
                out.append(out[src + k])
        else:
            raise ValueError(
                f"LC_LZ3.decompress: command {c:#04x} not emitted by this "
                f"encoder (offset {p - 1})"
            )
    return bytes(out)
