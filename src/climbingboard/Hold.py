import string
from typing import Tuple

from climbingboard.Comparable import Comparable
from climbingboard.Position import Position


class Hold(Comparable):
    position: Position
    name: str

    def __init__(self, name: str, position: Position):
        self.position = position
        self.name = name

    @property
    def _cmpkey(self) -> int:
        letter_index = string.ascii_uppercase.index(self.letter)
        number_index = int(self.number)
        return (number_index * 100) + letter_index

    @property
    def coordinates(self) -> Tuple[str, str]:
        return self.Coordinates(self.name)

    @property
    def letter(self) -> str:
        return self.Letter(self.name)

    @property
    def number(self) -> str:
        return self.Number(self.name)

    @staticmethod
    def Letter(name: str) -> str:
        letter = name[:1]
        if letter not in string.ascii_uppercase:
            raise ValueError("First character of hold name must be a capital letter")
        return letter

    @staticmethod
    def Number(name: str) -> str:
        number = name[1:]
        int(number)
        return number

    @classmethod
    def Coordinates(cls, name: str) -> Tuple[str, str]:
        return cls.Letter(name), cls.Number(name)

    def __repr__(self):
        return f" {self.name} ({self.position.x},{self.position.y})"
