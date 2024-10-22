from solution import parseInput, sortHandsQuickPass, refineSort
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

ROUGH_SORT_EXAMPLE = {
        "Five of a kind" : [],
        "Four of a kind" : [],
        "Full house" : [],
        "Three of a kind" : [{"cards" : "T55J5", "bid" : 684}, {"cards" : "QQQJA", "bid" : 483}],
        "Two pair" : [{"cards" : "KK677", "bid" : 28}, {"cards" : "KTJJT", "bid" : 220}],
        "One pair" : [{"cards" : "32T3K", "bid" : 765}],
        "High card" : []}

FINE_SORT_EXAMPLE = {
        "Five of a kind" : [],
        "Four of a kind" : [],
        "Full house" : [],
        "Three of a kind" : [{"cards" : "QQQJA", "bid" : 483}, {"cards" : "T55J5", "bid" : 684}],
        "Two pair" : [{"cards" : "KTJJT", "bid" : 220}, {"cards" : "KK677", "bid" : 28}],
        "One pair" : [{"cards" : "32T3K", "bid" : 765}],
        "High card" : []}

def testParsing():
    formattedInputAttempt = parseInput(PATH_EXAMPLE)
    assert formattedInputAttempt == FORMATTED_INPUT_EXAMPLE

def testRoughSort():
    roughlySorted = sortHandsQuickPass(FORMATTED_INPUT_EXAMPLE)
    assert roughlySorted == ROUGH_SORT_EXAMPLE

def refineSort():
    finelySorted = refineSort(ROUGH_SORT_EXAMPLE)
    assert finelySorted == FINE_SORT_EXAMPLE