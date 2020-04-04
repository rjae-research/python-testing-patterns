from uuid import uuid4

from core.email_address import EmailAddress

"""
AntiPattern: Class contains multiple responsibilities.

Validation of non-empty strings is not responsibility of User class.
"""
class User():

    def __init__(self, first_name: str, last_name: str, email_address: EmailAddress, id: uuid4 = None):
        if not first_name or not first_name.strip():
            raise ValueError(
                f"first_name cannot be null or whitespace: {first_name}")
        """
        Bug: LastName not also fixed when FirstName fixed to validate non-whitespace.

        Refactoring name validation to another class would centralize the behavior and drastically reduce risk of bugs.
        """
        if not last_name:
            raise ValueError(
                f"last_name cannot be null or whitespace: {last_name}")
        if not email_address:
            raise ValueError(
                f"email_address cannot be null: {email_address}")
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
        self._id = id if id else uuid4()

    @property
    def email_address(self) -> EmailAddress:
        return self._email_address

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def id(self) -> uuid4:
        return self._id

    @property
    def last_name(self) -> str:
        return self._last_name
