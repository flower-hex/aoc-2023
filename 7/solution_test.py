from solution import parseInput
import pytest

''' example input:
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

PATH_EXAMPLE = "7/example.txt"

FORMATTED_INPUT_EXAMPLE = [{"hand" : ["3", "2","T","3","K"], "bid" : 765}]

def testParsing():
    formattedInputAttempt = parseInput("32T3K 765")
    assert formattedInputAttempt == FORMATTED_INPUT_EXAMPLE