from Board import Board
from BoardPicture import BoardPicture
from BoulderProblemGeneration import BoulderProblemGeneration
from BoardService import BoardService

from configuration import hold_positions, missing_holds

if __name__ == "__main__":
  myBoard = Board(18, 12, 15, 15, missing_holds)
  myBoard.missing_holds.remove(myBoard.hold_from_name("H13"))

  myBoardPic = BoardPicture(myBoard, "houseboard.jpg", hold_positions)

  myGeneration = BoulderProblemGeneration(myBoard)
  random_problem = myGeneration.random_ascending(20, 70)
  myBoardPic.render(random_problem)

  myService = BoardService()
  myService.insert(random_problem)