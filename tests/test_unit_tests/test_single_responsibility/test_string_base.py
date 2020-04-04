import pytest

from core.string_base import StringBase


def test_init_must_set_value_when_value_is_none():
    assert StubString(None).value is None


def test_eq_must_return_false_when_other_is_none():
    assert StubString("Bob") != None


def test_eq_must_return_false_when_cased_is_false_and_other_value_is_not_equal():
    assert StubString("Bob", True, False) != StubString("Alice", True, False)


def test_eq_must_return_true_when_cased_is_false_and_other_value_is_equal():
    assert StubString("Bob", True, False) == StubString("bob", True, False)


def test_eq_must_return_false_when_cased_is_true_and_other_value_is_not_equal():
    assert StubString("Bob") != StubString("bob")


def test_eq_must_return_true_when_cased_is_true_and_other_value_is_equal():
    assert StubString("Bob") == StubString("Bob")


def test_gt_must_return_false_when_other_is_none():
    assert (StubString("B") > None) is False


def test_gt_must_return_false_when_cased_is_false_and_value_is_not_greater_than_other_value():
    assert (StubString("B", True, False) > StubString("c", True, False)) is False


def test_gt_must_return_true_when_cased_is_false_and_value_is_greater_than_other_value():
    assert StubString("B", True, False) > StubString("a", True, False)


def test_gt_must_return_false_when_cased_is_true_and_value_is_not_greater_than_other_value():
    assert (StubString("B") > StubString("C")) is False


def test_gt_must_return_true_when_cased_is_true_and_value_is_greater_than_other_value():
    assert StubString("B") > StubString("A")


def test_hash_must_return_same_result_when_cased_is_true_and_value_is_equal():
    assert hash(StubString("B")) == hash(StubString("B"))


def test_hash_must_return_different_result_when_cased_is_true_and_value_is_not_equal():
    assert hash(StubString("B")) != hash(StubString("b"))


def test_hash_must_return_same_result_when_cased_is_false_and_value_is_equal():
    assert hash(StubString("B", True, False)) == hash(StubString("b", True, False))


def test_hash_must_return_different_result_when_cased_is_false_and_value_is_not_equal():
    assert hash(StubString("B", True, False)) != hash(StubString("C", True, False))


def test_repr_must_return_expected_value_when_called():
    assert "value: '42'" == repr(StubString("42"))


def test_str_must_return_expected_value_when_called():
    assert "42" == str(StubString("42"))


class StubString(StringBase):

    def __init__(self, value: str, trimmed: bool = True, cased: bool = True):
        super().__init__(value, trimmed, cased)

    def _equals_(self, other) -> bool:
        return super()._equals_(other)

    def _greater_than_(self, other) -> bool:
        return super()._greater_than_(other)
