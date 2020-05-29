import pytest

from climbingboard.Board import Board
from climbingboard.BoulderProblemGeneration import BoulderProblemGeneration


def test_boulder_generation():
    myBoard = Board(18, 12, 15, 15, [])
    myGeneration = BoulderProblemGeneration(myBoard)
    random_problem = myGeneration.random_ascending(20, 70)
    assert len(random_problem) > 0
