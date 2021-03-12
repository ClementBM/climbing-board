import abc
from abc import ABC, abstractmethod, abstractproperty
from typing import List, Dict
from enum import Enum, unique
from typing import NamedTuple
import numpy as np
import string


@unique
class HoldGrasping(Enum):
    NONE = 0
    FOOT = 1
    HAND = 2
    BOTH = 3


class Position(NamedTuple):
    x: int
    y: int


class BoulderProblemGrade:
    mark: str


class HoldSpan(ABC):
    pass


class IHold(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError("Must provide implementation in subclass.")

    @property
    @abstractmethod
    def settings(self) -> dict:
        raise NotImplementedError("Must provide implementation in subclass.")

    def __add__(self, other) -> HoldSpan:
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)


class Hold(IHold):
    def __init__(
        self,
        name: str,
        settings: dict,
    ):
        self._name = name
        self._settings = settings

    def name(self):
        return self._name

    def settings(self):
        return self._settings


class NoHold(IHold):
    name = "No_Hold"
    settings: dict = {}


class Board:
    def __init__(
        self,
        horizontal_count: int,
        vertical_count: int,
        horizontal_spacing: float,
        vertical_spacing: float,
    ):
        self.horizontal_count = horizontal_count
        self.vertical_count = vertical_count
        self.grid = np.full((horizontal_count, vertical_count), NoHold())

        self.alpha_indices = string.ascii_uppercase[: self.horizontal_count]
        self.number_indices = list(range(1, vertical_count + 1)[::-1])

    def get_hold_by_alpha_num(self, alph_num) -> IHold:
        letter = alph_num[:1]
        number = int(alph_num[1:])

        hold: IHold = self.grid[
            self._letter_to_index(letter), self._number_to_index(number)
        ]
        return hold

    def _letter_to_index(self, letter: str) -> int:
        return self.alpha_indices.index(letter)

    def _number_to_index(self, number: int) -> int:
        return self.number_indices.index(number)


class BoulderProblem:
    name: str
    repeat_count: int
    is_benchmark: bool
    grade: BoulderProblemGrade
    user_grade: BoulderProblemGrade
    angle: int

    board: Board

    def __init__(
        self,
        board,
    ):
        self.holds_mask = np.full(
            (board.horizontal_count, board.vertical_count), HoldGrasping.NONE
        )
