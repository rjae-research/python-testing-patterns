from core.non_empty_string import NonEmptyString


class EmailAddress(NonEmptyString):

    def __init__(self, value: str):
        super().__init__(value, True, False)
        if not "@" in self.value:  # not for production use
            raise ValueError(f"{repr(self)} is not a valid email address")
