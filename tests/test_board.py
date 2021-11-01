import pytest
from climbing_board.main import Board, NoHold


def test_board_creation():

    my_board = Board(
        horizontal_count=12,
        vertical_count=18,
        horizontal_spacing=20.0,
        vertical_spacing=20.0,
    )

    a1 = my_board.get_hold_by_alpha_num("A1")
    a2 = my_board.get_hold_by_alpha_num("A2")

    hold_span = a1 - a2
    distance = hold_span.distance
    assert distance == 20.0


def test_create_board():
    board = pd.DataFrame(
        data={
            "A": [NoHold(), NoHold(), NoHold],
            "B": [NoHold(), NoHold(), NoHold],
            "C": [NoHold(), NoHold(), NoHold],
        }
    )

    assert board


def test_create_board_without_holds():
    df = pd.DataFrame(NoHold(), index=["1", "2", "3"], columns=["A", "B"])

    assert df
