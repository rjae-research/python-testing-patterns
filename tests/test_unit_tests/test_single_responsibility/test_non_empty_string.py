import pytest

from core.non_empty_string import NonEmptyString


def test_init_must_not_strip_value_when_trimmed_is_false():
    assert " @ " == NonEmptyString(" @ ", False).value


@pytest.mark.parametrize("value", [(None), (""), ("    "), ("\t")])
def test_init_must_raise_error_when_value_is_invalid(value: str):
    expected = value if value is None else repr(value.strip())
    with pytest.raises(ValueError, match=f"value: {expected} cannot be empty"):
        NonEmptyString(value)


def test_eq_must_return_true_when_other_is_equal():
    assert NonEmptyString("Bob") == NonEmptyString("Bob")


def test_eq_must_return_false_when_other_is_equal():
    assert NonEmptyString("Bob") != NonEmptyString("bob")


def test_gt_than_must_return_true_when_value_is_greater_than_other_value():
    assert NonEmptyString("B") > NonEmptyString("A")


def test_gt_than_must_return_false_when_value_is_not_greater_than_other_value():
    assert (NonEmptyString("B") > NonEmptyString("B")) is False
