import abc
from abc import ABC, abstractmethod, abstractproperty
from typing import List, Dict
from enum import Enum, unique
from typing import NamedTuple
import numpy as np
import string
import pandas as pd


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
        settings: dict = {},
    ):
        self._name = name
        self._settings = settings

    @property
    def name(self):
        return self._name

    @property
    def settings(self):
        return self._settings

    def __repr__(self):
        return self.name


class NoHold(IHold):
    name = "No_Hold"
    settings: dict = {}

    def __repr__(self):
        return self.name


class Board:
    def __init__(
        self,
        horizontal_count: int,
        vertical_count: int,
        horizontal_spacing: float,
        vertical_spacing: float,
    ):
        """
        :horizontal_spacing: mm
        :vertical_spacing: mm
        """
        self.horizontal_count = horizontal_count
        self.vertical_count = vertical_count

        self.horizontal_spacing = horizontal_spacing
        self.vertical_spacing = vertical_spacing

        self.alpha_indices = list(string.ascii_uppercase[: self.horizontal_count])

        self.number_indices = list(range(1, vertical_count + 1)[::-1])

        self.grid = pd.DataFrame(
            NoHold(),
            index=zip(
                self.number_indices,
                [
                    vertical * vertical_spacing
                    for vertical in range(self.vertical_count)[::-1]
                ],
            ),
            columns=zip(
                self.alpha_indices,
                [
                    horizontal * horizontal_spacing
                    for horizontal in range(self.horizontal_count)
                ],
            ),
        )

    def get_hold_by_alpha_num(self, alph_num) -> IHold:
        letter, number = self._split_alpha_num(alph_num)

        hold: IHold = self.grid.iloc[
            self.number_indices.index(number), self.alpha_indices.index(letter)
        ]
        return hold

    def add_hold_by_alpha_num(self, alph_num, hold: IHold):
        letter, number = self._split_alpha_num(alph_num)

        self.grid.iloc[
            self.number_indices.index(number), self.alpha_indices.index(letter)
        ] = hold

    def _letter_to_index(self, letter: str):
        return letter, self.horizontal_spacing * self.alpha_indices.index(letter)

    def _number_to_index(self, number: int):
        return number, self.vertical_spacing * self.number_indices.index(number)

    def _split_alpha_num(self, alph_num):
        letter = alph_num[:1]
        number = int(alph_num[1:])
        return letter, number

    def get_distance(self, hold_1, hold_2):
        coord_1 = self._get_coord_from_hold(hold_1)
        coord_2 = self._get_coord_from_hold(hold_2)
        return 0

    def _get_coord_from_hold(self, alpha_num_value):
        letter, number = self._split_alpha_num(alpha_num_value)
        x = [i for i in self.grid.index if i[0] == number][0][1]
        y = [i for i in self.grid.columns if i[0] == letter][0][1]

        return Position(x=x, y=y)

    def __repr__(self):
        return repr(self.grid)


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
