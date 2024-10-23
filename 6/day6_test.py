import day6_solution
import pytest

"""
example input
Time:      7  15   30
Distance:  9  40  200
"""
FORMATTED_INPUT_EXAMPLE = [{'time': 7, 'distance': 9}, {'time': 15, 'distance': 40}, {'time': 30, 'distance': 200}]

FORMATTED_INPUT_EXAMPLE2 = [{'time': 71530, 'distance': 940200}]

MULTIPLES_EXAMPLE = [4, 8, 9]

SOLUTION_EXAMPLE = 288

def testParsing():
  result = day6_solution.parseInput("6/example.txt")
  assert result == FORMATTED_INPUT_EXAMPLE

def testParsing2():
  result = day6_solution.parseInput2("6/example.txt")
  assert result == FORMATTED_INPUT_EXAMPLE2

def testExampleMultiplication():
  result = day6_solution.solveInput(FORMATTED_INPUT_EXAMPLE)
  assert result == SOLUTION_EXAMPLE

@pytest.mark.parametrize("time,distance,expected", [
  (7, 9, 4),
  (15, 40, 8),
  (30, 200, 9),
  (71530, 940200, 71503)
])
def testExampleRecord(time, distance, expected):
  result = day6_solution.solveRace(time, distance)
  assert result == expected

# ty hannah!