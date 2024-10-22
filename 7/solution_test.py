from solution import parseInput, sortHands, solveSorted
import pytest

''' example input:
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

PATH_EXAMPLE = "7/example.txt"

FORMATTED_INPUT_EXAMPLE = [{"cards" : "32T3K", "bid" : 765},
                           {"cards" : "T55J5", "bid" : 684},
                           {"cards" : "KK677", "bid" : 28},
                           {"cards" : "KTJJT", "bid" : 220},
                           {"cards" : "QQQJA", "bid" : 483}]

SORT_EXAMPLE = [
        [], # High card
        [{"cards" : "32T3K", "bid" : 765}], # One pair
        [{"cards" : "KTJJT", "bid" : 220},
         {"cards" : "KK677", "bid" : 28}], # Two pair
        [{"cards" : "T55J5", "bid" : 684},
         {"cards" : "QQQJA", "bid" : 483}], # Three of a kind
        [], # Full house
        [], # Four of a kind
        []] # Five of a kind

SOLUTION_EXAMPLE = 6440

def testParsing():
    formattedInputAttempt = parseInput(PATH_EXAMPLE)
    assert formattedInputAttempt == FORMATTED_INPUT_EXAMPLE

def testSortHands():
    roughlySorted = sortHands(FORMATTED_INPUT_EXAMPLE)
    assert roughlySorted == SORT_EXAMPLE

def testSolveSorted():
    outputSum = solveSorted(SORT_EXAMPLE)
    assert outputSum == SOLUTION_EXAMPLE