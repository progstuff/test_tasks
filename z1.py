from dataclasses import dataclass
from functools import total_ordering
from typing import ClassVar


@total_ordering
@dataclass(frozen=True)
class Technic:
    name: str
    price: float
    availability: bool
    __PRICE_LIMIT: ClassVar[float] = 200

    def category(self) -> str:
        return "Бюджетный" if self.price > self.__PRICE_LIMIT else "Дорогой"

    def __lt__(self, other):
        return len(self.name) < len(other.name)

    def __le__(self, other):
        return len(self.name) <= len(other.name)

    def __eq__(self, other):
        return len(self.name) == len(other.name)

    # def __gt__(self, other):
    #    return len(self.name) > len(other.name)

    # def __ge__(self, other):
    #    return len(self.name) >= len(other.name)

    # def __ne__(self, other):
    #    return len(self.name) != len(other.name)
