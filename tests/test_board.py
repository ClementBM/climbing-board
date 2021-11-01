import pytest
from climbing_board.main import Board, NoHold, Hold
import pandas as pd


@pytest.fixture
def empty_board():
    return Board(
        horizontal_count=11,
        vertical_count=18,
        horizontal_spacing=100,
        vertical_spacing=100,
    )


def test_create_empty_board(empty_board):
    assert empty_board


def test_check_get_hold_by_coord(empty_board: Board):
    new_hold = Hold(name="A1")
    empty_board.add_hold_by_alpha_num(alph_num="A1", hold=new_hold)
    hold = empty_board.get_hold_by_alpha_num("A1")
    assert hold == new_hold


def test_board_creation(empty_board: Board):
    distance = empty_board.get_distance("A2", "A1")

    assert distance == 20.0