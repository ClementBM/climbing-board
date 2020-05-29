from typing import Dict, Tuple, List

# from Board import Board
from climbingboard.Hold import Hold
from climbingboard.Position import Position
from climbingboard.Board import Board

from skimage import io
from skimage.draw import circle_perimeter
import matplotlib.pyplot as plt


class BoardPicture:
    board: Board
    picture_path: str
    hold_positions: Dict[str, Tuple[int, int]]

    def __init__(
        self,
        board: Board,
        picture_path: str,
        hold_positions: Dict[str, Tuple[int, int]],
    ):
        self.board = board
        self.picture_path = picture_path
        self.hold_positions = hold_positions

    def render(self, holds: List[Hold]):
        plt.figure(figsize=(14, 10))
        image = io.imread(self.picture_path)
        for hold in holds:
            self.render_circle(image, hold)
        io.imshow(image)
        plt.show()

    def render_circle(self, image, hold: Hold):
        hold_position = self.circle_from_position(hold)
        for i in range(5):
            r, c = circle_perimeter(hold_position.x, hold_position.y, 24 + i)
            image[r, c, :] = (255, 1, 0)

    def circle_from_position(self, hold: Hold) -> Position:
        x, y = self.hold_positions[hold.name]
        return Position(int(y), int(x))
