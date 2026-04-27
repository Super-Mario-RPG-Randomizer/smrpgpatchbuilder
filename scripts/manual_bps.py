"""Hand-rolled minimal BPS encoder. Walks source/target in chunked
strides and emits a sequence of SourceRead / TargetRead ops.

Avoids the costly delta search of the upstream bps.diff implementation,
which doesn't terminate in reasonable time when a large fraction of the
target consists of zero runs (as happens when SpriteCollection.render()
zeroes whole tile/animation banks before refilling them).
"""
from zlib import crc32
from bps import operations as ops


def _equal_run(source: bytes, target: bytes, start: int, end: int) -> int:
    """Return the index just past the longest run of equal bytes from start, capped at end."""
    n = end
    i = start
    # Compare in chunks for speed; bytes equality is implemented in C.
    chunk = 4096
    while i + chunk <= n and source[i:i+chunk] == target[i:i+chunk]:
        i += chunk
    while i < n and source[i] == target[i]:
        i += 1
    return i


def _diff_run(source: bytes, target: bytes, start: int, end: int) -> int:
    """Return the index just past the longest run of differing bytes from start, capped at end."""
    n = end
    i = start
    chunk = 4096
    while i + chunk <= n:
        if source[i:i+chunk] == target[i:i+chunk]:
            break
        i += chunk
    while i < n and source[i] != target[i]:
        i += 1
    # Pull back into the boundary chunk to find the exact transition.
    return i


def diff_simple(source: bytes, target: bytes, metadata: str = ""):
    """Yield BPS ops that transform source into target using only
    SourceRead and TargetRead ops (and the required CRC trailers).
    """
    yield ops.Header(len(source), len(target), metadata)

    n = min(len(source), len(target))
    i = 0
    while i < n:
        if source[i] == target[i]:
            j = _equal_run(source, target, i, n)
            if j > i:
                yield ops.SourceRead(j - i)
            i = j
        else:
            j = _diff_run(source, target, i, n)
            if j > i:
                yield ops.TargetRead(bytes(target[i:j]))
            i = j

    if len(target) > n:
        yield ops.TargetRead(bytes(target[n:]))

    yield ops.SourceCRC32(crc32(source))
    yield ops.TargetCRC32(crc32(target))
