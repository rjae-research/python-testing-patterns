from uuid import uuid4

from core.email_address import EmailAddress
from core.non_empty_string import NonEmptyString
from core.not_none import not_none


class User():

    def __init__(self, first_name: NonEmptyString, last_name: NonEmptyString, email_address: EmailAddress, id: uuid4 = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.id = id if id else uuid4()

    @property
    def email_address(self) -> EmailAddress:
        return self._email_address

    @email_address.setter
    @not_none
    def email_address(self, value):
        self._email_address = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    @not_none
    def first_name(self, value):
        self._first_name = value

    @property
    def id(self) -> uuid4:
        return self._id

    @id.setter
    @not_none
    def id(self, value):
        self._id = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    @not_none
    def last_name(self, value):
        self._last_name = value
