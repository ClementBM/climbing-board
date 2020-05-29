from climbingboard.Board import Board
from climbingboard.BoardPicture import BoardPicture
from climbingboard.BoulderProblemGeneration import BoulderProblemGeneration
from climbingboard.BoardService import BoardService

from climbingboard.configuration import hold_positions, missing_holds

if __name__ == "__main__":
    myBoard = Board(18, 12, 15, 15, missing_holds)
    myBoard.missing_holds.remove(myBoard.hold_from_name("H13"))

    myBoardPic = BoardPicture(myBoard, "houseboard.jpg", hold_positions)

    myGeneration = BoulderProblemGeneration(myBoard)
    random_problem = myGeneration.random_ascending(20, 70)
    myBoardPic.render(random_problem)

    myService = BoardService()
    myService.insert(random_problem)
