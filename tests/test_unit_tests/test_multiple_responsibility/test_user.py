from uuid import uuid4

import pytest

from core.email_address import EmailAddress
from core.non_empty_string import NonEmptyString
from core.string_base import StringBase
from anti_patterns.multiple_responsibility.user import User


"""
AntiPattern: Module contains multiple responsibilities:

* Contains tests for multiple classes.
* Changes when either User, EmailAddress, NonEmptyString, or StringBase changes.
* Difficult to identity which tests are for which class.
"""


def test_init_must_strip_value_when_trimmed_is_true():
    assert "@" == EmailAddress(" @ ").value


def test_init_must_not_strip_value_when_trimmed_is_false():
    assert " @ " == NonEmptyString(" @ ", False).value


def test_init_must_set_value_when_value_is_none():
    assert StubString(None).value is None


@pytest.mark.parametrize("value", [(None), (""), ("    "), ("\t")])
def test_init_must_raise_error_when_value_is_invalid(value: str):
    expected = value if value is None else repr(value.strip())
    with pytest.raises(ValueError, match=f"value: {expected} cannot be empty"):
        NonEmptyString(value)


@pytest.mark.parametrize("value", [("bad")])
def test_init_must_raise_error_when_email_address_is_invalid(value: str):
    with pytest.raises(ValueError, match=f"value: '{value}' is not a valid email address"):
        EmailAddress(value)


@pytest.mark.parametrize("value", [(None), (""), ("    "), ("\t")])
def test_init_must_raise_error_when_first_name_is_invalid(value: str):
    with pytest.raises(ValueError, match=f"first_name cannot be null or whitespace: {value}"):
        User(value, "Smith", "@")


@pytest.mark.parametrize("value", [(None), ("")])
def test_init_must_raise_error_when_last_name_is_invalid(value: str):
    with pytest.raises(ValueError, match=f"last_name cannot be null or whitespace: {value}"):
        User("Bob", value, "@")


@pytest.mark.parametrize("value", [(None)])
def test_init_must_raise_error_when_user_email_address_is_invalid(value: str):
    with pytest.raises(ValueError, match=f"email_address cannot be null: {value}"):
        User("Bob", "Smith", value)


def test_init_must_set_email_address_when_email_address_is_valid():
    assert "@" == User("Bob", "Smith", "@").email_address


def test_init_must_set_first_name_when_first_name_is_valid():
    assert "Bob" == User("Bob", "Smith", "@").first_name


def test_init_must_set_id_when_id_is_specified():
    id: uuid4 = uuid4()
    assert id == User("Bob", "Smith", "@", id).id


def test_init_must_set_last_name_when_last_name_is_valid():
    assert "Smith" == User("Bob", "Smith", "@").last_name


def test_init_must_set_value_when_email_address_is_valid():
    assert "@" == EmailAddress("@").value


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


def test_eq_must_return_true_when_other_is_equal():
    assert NonEmptyString("Bob") == NonEmptyString("Bob")


def test_eq_must_return_false_when_other_is_equal():
    assert NonEmptyString("Bob") != NonEmptyString("bob")


def test_gt_than_must_return_true_when_value_is_greater_than_other_value():
    assert NonEmptyString("B") > NonEmptyString("A")


def test_gt_than_must_return_false_when_value_is_not_greater_than_other_value():
    assert (NonEmptyString("B") > NonEmptyString("B")) is False


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
