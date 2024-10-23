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

OUTPUT_EXAMPLE = 2
OUTPUT_EXAMPLE_2 = 6

@pytest.mark.parametrize("input,expected_directions,expected_network", [
  ("8/example.txt", FORMATTED_DIRECTIONS_EXAMPLE, FORMATTED_NETWORK_EXAMPLE),
  ("8/example2.txt", FORMATTED_DIRECTIONS_EXAMPLE_2, FORMATTED_NETWORK_EXAMPLE_2)
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