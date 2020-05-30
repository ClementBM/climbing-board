from climbingboard.board import Board
from climbingboard.boardpicture import BoardPicture
from climbingboard.boulderproblemgeneration import BoulderProblemGeneration
from climbingboard.boardservice import BoardService

from climbingboard.configuration import HOLD_POSITIONS, MISSING_HOLDS

if __name__ == "__main__":
    myBoard = Board(18, 12, 15, 15, MISSING_HOLDS)
    myBoard.missing_holds.remove(myBoard.hold_from_name("H13"))

    myBoardPic = BoardPicture(myBoard, "houseboard.jpg", HOLD_POSITIONS)

    myGeneration = BoulderProblemGeneration(myBoard)
    random_problem = myGeneration.random_ascending(20, 70)
    myBoardPic.render(random_problem)

    myService = BoardService()
    myService.insert(random_problem)
