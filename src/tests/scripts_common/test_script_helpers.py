import pytest

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptCommandNoArgs,
    TransformableIdentifier,
)


class _Cmd(ScriptCommandNoArgs):
    _opcode = 0xFE


def _labels(script: Script) -> list[str]:
    return [cmd.identifier.label for cmd in script.contents]


def test_insert_before_identifier_inserts_before():
    script = Script([_Cmd(identifier="first"), _Cmd(identifier="second")])
    script.insert_before_identifier("second", _Cmd(identifier="new"))
    assert _labels(script) == ["first", "new", "second"]


def test_insert_after_identifier_inserts_after():
    script = Script([_Cmd(identifier="first"), _Cmd(identifier="second")])
    script.insert_after_identifier("first", _Cmd(identifier="new"))
    assert _labels(script) == ["first", "new", "second"]


def test_get_index_of_identifier_error_includes_name():
    script = Script([_Cmd(identifier="only")])
    with pytest.raises(IdentifierException, match="nonexistent not found"):
        script.get_index_of_identifier("nonexistent")


def test_illegal_jump_does_not_skip_remaining_destinations():
    bank = ScriptBank(None)
    bank.addresses["real_label"] = 0x0C0B
    illegal = TransformableIdentifier("ILLEGAL_JUMP_1234")
    real = TransformableIdentifier("real_label")
    bank._set_identifier_addresses([illegal, real])
    assert illegal.address == 0x1234
    assert real.address == 0x0C0B
