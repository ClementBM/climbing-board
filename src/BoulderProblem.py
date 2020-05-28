from os import linesep
from typing import List

from BoulderProblemHold import BoulderProblemHold


class BoulderProblem:
    hold_sequence: List[BoulderProblemHold]
    grade: str
    name: str
    user_grade: str
    repeat_count: int
    is_benchmark: bool

    def __init__(
        self,
        hold_sequence: List[BoulderProblemHold],
        grade: str,
        name: str,
        user_grade: str,
        repeat_count: int,
        is_benchmark,
        setup,
    ):
        self.hold_sequence = hold_sequence
        self.grade = grade
        self.name = name
        self.user_grade = user_grade
        self.repeat_count = repeat_count
        self.is_benchmark = is_benchmark
        self.setup = setup

    def __repr__(self):
        sequence_strings = [repr(hold) for hold in self.hold_sequence]
        return f"{self.grade} '{self.name}', repeats:{self.repeat_count}, benchmark:{self.is_benchmark}, setup:{self.setup}{linesep}{linesep.join(sequence_strings)}"
