from uuid import uuid4

import pytest

from patterns.single_responsibility.user import User

"""
Compare this module with tests.test_multiple_responsibility.test_user.
You can clearly see how this module tests a single vector of change.
Imagine handing this module to another developer vs. the other module.
"""


def test_init_must_raise_error_when_first_name_is_invalid():
    with pytest.raises(ValueError, match="first_name cannot be None"):
        User(None, "Smith", "@")


def test_init_must_raise_error_when_last_name_is_invalid():
    with pytest.raises(ValueError, match="last_name cannot be None"):
        User("Bob", None, "@")


def test_init_must_raise_error_when_user_email_address_is_invalid():
    with pytest.raises(ValueError, match="email_address cannot be None"):
        User("Bob", "Smith", None)


def test_init_must_set_email_address_when_email_address_is_valid():
    assert "@" == User("Bob", "Smith", "@").email_address


def test_init_must_set_first_name_when_first_name_is_valid():
    assert "Bob" == User("Bob", "Smith", "@").first_name


def test_init_must_set_id_when_id_is_specified():
    id: uuid4 = uuid4()
    assert id == User("Bob", "Smith", "@", id).id


def test_init_must_set_last_name_when_last_name_is_valid():
    assert "Smith" == User("Bob", "Smith", "@").last_name
