import pytest
import sys
sys.path.append('src')

from Board import Board
from BoulderProblemGeneration import BoulderProblemGeneration

def test_boulder_generation():
  myBoard = Board(18, 12, 15, 15, [])
  
  myGeneration = BoulderProblemGeneration(myBoard)
  random_problem = myGeneration.random_ascending(20, 70)
  assert len(random_problem) > 0
