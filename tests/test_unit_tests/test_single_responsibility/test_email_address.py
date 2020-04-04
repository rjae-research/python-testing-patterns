import pytest

from core.email_address import EmailAddress


def test_init_must_strip_value_when_trimmed_is_true():
    assert "@" == EmailAddress(" @ ").value


@pytest.mark.parametrize("value", [("bad")])
def test_init_must_raise_error_when_email_address_is_invalid(value: str):
    with pytest.raises(ValueError, match=f"value: '{value}' is not a valid email address"):
        EmailAddress(value)


def test_init_must_set_value_when_email_address_is_valid():
    assert "@" == EmailAddress("@").value
