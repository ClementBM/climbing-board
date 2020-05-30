import pytest

from climbingboard.board import Board
from climbingboard.boulderproblemgeneration import BoulderProblemGeneration


def test_boulder_generation():
    myBoard = Board(18, 12, 15, 15, [])
    myGeneration = BoulderProblemGeneration(myBoard)
    length_max = 20
    random_problem = myGeneration.random_ascending(length_max, 70)

    assert len(random_problem) > 0
    assert len(random_problem) <= length_max
