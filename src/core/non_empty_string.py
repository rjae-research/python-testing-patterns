from core.string_base import StringBase


class NonEmptyString(StringBase):

    def __init__(self, value: str, trimmed: bool = True, cased: bool = True):
        super().__init__(value, trimmed, cased)
        if not self.value:
            raise ValueError(f"{repr(self)} cannot be empty")

    def _equals_(self, other) -> bool:
        return super()._equals_(other)

    def _greater_than_(self, other) -> bool:
        return super()._greater_than_(other)
