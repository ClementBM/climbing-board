import pytest
import os

from climbingboard.board import Board
from climbingboard.hold import Hold
from climbingboard.holdkind import HoldKind
from climbingboard.position import Position
from climbingboard.boulderproblemhold import BoulderProblemHold


def test_hold_management():
    h1 = Hold("A1", Position(1, 1))
    assert h1 == h1
    h2 = Hold("A1", Position(1, 2))
    assert h1 == h2
    assert h2 == h1

    bph1 = BoulderProblemHold("A1", Position(1, 1), HoldKind.FOOT)
    assert h1 != bph1
    assert bph1 != h1

    bph2 = BoulderProblemHold("A1", Position(1, 1), HoldKind.HAND)
    bph3 = BoulderProblemHold("A1", Position(1, 2), HoldKind.HAND)

    assert bph1 != bph2
    assert bph2 == bph3


def test_hold_sorting():
    myBoard = Board(18, 12, 15, 15, [])
    holds = [myBoard.hold_from_name(hold) for hold in ["A1", "B1", "E12", "H5", "A1"]]
    sorted_holds = sorted(holds)
    expected_sorted_holds = holds = [
        myBoard.hold_from_name(hold) for hold in ["A1", "A1", "B1", "H5", "E12"]
    ]

    assert expected_sorted_holds == sorted_holds
