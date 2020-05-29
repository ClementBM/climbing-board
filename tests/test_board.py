import pytest
from climbingboard.Board import Board


def test_board_creation():
    myBoard = Board(18, 12, 15, 15, [])
    a1 = myBoard.hold_from_name("A1")
    a2 = myBoard.hold_from_name("A2")
    distance = myBoard.distance(a1, a2)
    assert distance == 15.0
