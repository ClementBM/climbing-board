import random
from typing import List

from climbingboard.board import Board
from climbingboard.hold import Hold


class BoulderProblemGeneration:
    board: Board
    available_holds: List[Hold]
    first_holds: List[Hold]

    def __init__(self, board: Board):
        self.board = board
        self.available_holds = list(
            set(self.board.holds) - set(self.board.missing_holds)
        )
        self.first_holds = [
            hold
            for hold in self.available_holds
            if hold.number in [str(i) for i in range(3, 11)]
        ]

    def random_ascending(self, length_max: int, distance_max: float) -> List[Hold]:
        first_hold = random.choice(self.first_holds)
        holds = [first_hold]

        while (
            len(holds) < length_max and holds[-1].number != self.board.holds[-1].number
        ):
            hold = random.choice(self.available_holds)
            distance = self.board.distance(holds[-1], hold)
            if distance > distance_max:
                continue
            if hold in holds:
                continue
            if self.board.is_hold_upper_or_equal(holds[-1], hold):
                holds.append(hold)

        holds_ordered = self.board.order_hold_sequence(holds)
        return holds_ordered
