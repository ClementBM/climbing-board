import pytest
import os

from climbingboard.BoardService import BoardService
from climbingboard.Board import Board


def test_database():
    try:
        db_name = "db_test.json"
        table_name = "table_test"
        myService = BoardService(db_name, table_name)

        myBoard = Board(18, 12, 15, 15, [])
        test_sequence = ["A1", "C4", "G9", "D12"]
        test_hold_sequence = [myBoard.hold_from_name(x) for x in test_sequence]
        id = myService.insert(test_hold_sequence)
        record = myService.get_by_id(id)
        assert record["sequence"] == test_sequence

        myService.remove(id)
        all_records = myService.get_all()
        assert len(all_records) == 0

        test_hash = hash("".join(test_sequence))
        myService.insert(test_hold_sequence)
        record = myService.get_by_hash(test_hash)
        assert record["sequence"] == test_sequence
    finally:
        os.remove(db_name)
