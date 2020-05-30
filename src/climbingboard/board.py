import string
from math import hypot
from typing import List, Tuple

from climbingboard.hold import Hold
from climbingboard.position import Position


class Board:
    vertical_count: int
    horizontal_count: int
    vertical_spacing: int
    horizontal_spacing: int
    missing_holds: List[Hold]
    holds: List[Hold]

    def __init__(
        self,
        vertical_count: int,
        horizontal_count: int,
        vertical_spacing: int,
        horizontal_spacing: int,
        missing_holds: List[str],
    ):
        self.horizontal_count = horizontal_count
        self.alpha_indices = string.ascii_uppercase[: self.horizontal_count]
        self.digit_indices = range(1, vertical_count + 1)[::-1]

        self.vertical_spacing = vertical_spacing
        self.horizontal_spacing = horizontal_spacing

        hold_list = [
            alpha + str(digit)
            for digit in range(1, vertical_count + 1)
            for alpha in self.alpha_indices
        ]
        self.holds = [self.hold_from_name(hold) for hold in hold_list]

        self.missing_holds = [self.hold_from_name(hold) for hold in missing_holds]

        # is symetric
        for missing_hold in missing_holds:
            opposite_hold = self._opposite_hold(missing_hold)
            if opposite_hold not in self.missing_holds:
                self.missing_holds.append(self.hold_from_name(opposite_hold))

    def hold_from_name(self, name: str) -> Hold:
        return Hold(name, self._hold_position(name))

    def _opposite_hold(self, hold: str) -> str:
        letter_index, number = self._hold_coords(hold)
        if self.horizontal_count % 2 != 0 and letter_index == (
            (self.horizontal_count - 1) / 2
        ):
            return hold
        if letter_index < (self.horizontal_count / 2):
            return f"{self.alpha_indices[-(letter_index+1)]}{number}"
        else:
            return f"{self.alpha_indices[self.horizontal_count-1-letter_index]}{number}"

    def is_hold_on_board(self, hold: Hold) -> None:
        if hold.name not in [hold.name for hold in self.holds]:
            raise ValueError("This hold does not exist on this board")

    def _hold_coords(self, hold: str) -> Tuple[int, int]:
        letter, number = Hold.Coordinates(hold)
        letter_index = string.ascii_uppercase.index(letter)
        return letter_index, int(number)

    def _hold_position(self, hold: str) -> Position:
        letter_index, number = self._hold_coords(hold)
        x = letter_index * self.horizontal_spacing
        y = number * self.vertical_spacing
        return Position(x, y)

    def order_hold_sequence(self, holds: List[Hold]) -> List[Hold]:
        holds.sort(key=lambda x: self.holds.index(x))
        return holds

    def distance(self, hold_1: Hold, hold_2: Hold) -> float:
        d_x = hold_2.position.x - hold_1.position.x
        d_y = hold_2.position.y - hold_1.position.y
        return hypot(d_x, d_y)

    def is_hold_upper_or_equal(self, hold_1: Hold, hold_2: Hold) -> bool:
        return hold_1.position.y <= hold_2.position.y
