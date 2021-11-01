import typing

from abc import ABC


class IHold(ABC):
    """
    A hold is a piece of something, can be made of wood,
    resin. On its own, is not connected or bolted onto anything
    until it is connected to a board.
    """

    name: str
    code: str  # unique


class IHoldPosition(ABC):
    """
    Hold position, where a hold can be installed.
    """

    x: int
    y: int


class IBoard(ABC):
    """
    A plan board on which hole has been drilled to fix some holds
    """

    hold_positions: typing.List[IHoldPosition]
    holds: typing.List[IHold]
    settings: dict


class IBoulderProblem(ABC):
    """
    Sequence of holds positionned on holes on a board.
    """

    pass
