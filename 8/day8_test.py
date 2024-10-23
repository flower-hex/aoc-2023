import pytest
from day8_solution import parseInput

FORMATTED_INPUT_DIRECTIONS_EXAMPLE = [1,0] # no native bit field type sadface

FORMATTED_INPUT_NETWORK_EXAMPLE = {"AAA" : ("BBB", "CCC"),
                                   "BBB" : ("DDD", "EEE"),
                                   "CCC" : ("ZZZ", "GGG"),
                                   "DDD" : ("DDD", "DDD"),
                                   "EEE" : ("EEE", "EEE"),
                                   "GGG" : ("GGG", "GGG"),
                                   "ZZZ" : ("ZZZ", "ZZZ"),}

FORMATTED_INPUT_DIRECTIONS_EXAMPLE_2 = [0,0,1]

FORMATTED_INPUT_NETWORK_EXAMPLE_2 = {"AAA" : ("BBB", "BBB"),
                                     "BBB" : ("AAA", "ZZZ"),
                                     "ZZZ" : ("ZZZ", "ZZZ")}

@pytest.mark.parametrize("input,expected_directions,expected_network", [
  ("8/example", FORMATTED_INPUT_DIRECTIONS_EXAMPLE, FORMATTED_INPUT_NETWORK_EXAMPLE),
  ("8/example2", FORMATTED_INPUT_DIRECTIONS_EXAMPLE_2, FORMATTED_INPUT_NETWORK_EXAMPLE_2)
])
def test_input_format_directions(input,expected_directions,expected_network):
    results = parseInput(input)
    assert results == expected_directions, expected_network

