import pytest
import day8_solution

FORMATTED_DIRECTIONS_EXAMPLE = [1,0] # no native bit field type sadface

FORMATTED_NETWORK_EXAMPLE = {"AAA" : ("BBB", "CCC"),
                             "BBB" : ("DDD", "EEE"),
                             "CCC" : ("ZZZ", "GGG"),
                             "DDD" : ("DDD", "DDD"),
                             "EEE" : ("EEE", "EEE"),
                             "GGG" : ("GGG", "GGG"),
                             "ZZZ" : ("ZZZ", "ZZZ"),}

FORMATTED_DIRECTIONS_EXAMPLE_2 = [0,0,1]

FORMATTED_NETWORK_EXAMPLE_2 = {"AAA" : ("BBB", "BBB"),
                               "BBB" : ("AAA", "ZZZ"),
                               "ZZZ" : ("ZZZ", "ZZZ")}

FORMATTED_DIRECTIONS_EXAMPLE_3 = [0,1]

FORMATTED_NETWORK_EXAMPLE_3 = {"11A" : ("11B", "XXX"),
                               "11B" : ("XXX", "11Z"),
                               "11Z" : ("11B", "XXX"),
                               "22A" : ("22B", "XXX"),
                               "22B" : ("22C", "22C"),
                               "22C" : ("22Z", "22Z"),
                               "22Z" : ("22B", "22B"),
                               "XXX" : ("XXX", "XXX")}

OUTPUT_EXAMPLE = 2
OUTPUT_EXAMPLE_2 = 6
OUTPUT_EXAMPLE_3 = 6

START_POINTS_3 = {"11A", "22A"}
END_POINTS_3 = {"11Z", "22Z"}

@pytest.mark.parametrize("input,expected_directions,expected_network", [
  ("8/example.txt", FORMATTED_DIRECTIONS_EXAMPLE, FORMATTED_NETWORK_EXAMPLE),
  ("8/example2.txt", FORMATTED_DIRECTIONS_EXAMPLE_2, FORMATTED_NETWORK_EXAMPLE_2),
  ("8/example3.txt", FORMATTED_DIRECTIONS_EXAMPLE_3, FORMATTED_NETWORK_EXAMPLE_3)
])
def test_input_format_directions(input,expected_directions,expected_network):
    results = day8_solution.parseInput(input)
    assert results == (expected_directions, expected_network)

@pytest.mark.parametrize("directions,network, expected_result", [
  (FORMATTED_DIRECTIONS_EXAMPLE, FORMATTED_NETWORK_EXAMPLE, OUTPUT_EXAMPLE),
  (FORMATTED_DIRECTIONS_EXAMPLE_2, FORMATTED_NETWORK_EXAMPLE_2, OUTPUT_EXAMPLE_2)
])
def test_traverseNetwork(directions,network, expected_result):
    result = day8_solution.traverseNetwork(directions,network, day8_solution.STARTPOINT, day8_solution.ENDPOINT)
    assert result == expected_result

def test_findStartEndPoints():
    result = day8_solution.findStartEndPoints(FORMATTED_NETWORK_EXAMPLE_3)
    assert result == (START_POINTS_3, END_POINTS_3)

def test_traverseNetwork_part2():
    result = day8_solution.traverseNetwork(FORMATTED_DIRECTIONS_EXAMPLE_3,FORMATTED_NETWORK_EXAMPLE_3, START_POINTS_3, END_POINTS_3)
    assert result == OUTPUT_EXAMPLE_3