from abc import ABC, abstractmethod


class StringBase(ABC):

    def __init__(self, value: str, trimmed: bool = True, cased: bool = True):
        self._value = value if not value or not trimmed else value.strip()
        self._cased = cased

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return other is not None and self._equals_(other)

    @abstractmethod
    def _equals_(self, other) -> bool:
        if not self._cased and not other._cased:
            return self.value.casefold() == other.value.casefold()
        else:
            return self.value == other.value

    def __gt__(self, other) -> bool:
        return other is not None and self._greater_than_(other)

    @abstractmethod
    def _greater_than_(self, other) -> bool:
        if not self._cased and not other._cased:
            return self.value.casefold() > other.value.casefold()
        else:
            return self.value > other.value

    def __hash__(self) -> int:
        return hash(self.value) if self._cased else hash(self.value.casefold())

    def __repr__(self) -> str:
        return f"value: {repr(self.value)}"

    def __str__(self) -> str:
        return str(self.value)
