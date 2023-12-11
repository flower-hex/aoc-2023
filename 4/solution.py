def card_reader(filename):
    with open(filename) as rawtxt:
        running_total = 0
        for line in rawtxt:
            start_of_line = line.index(":") + 1
            winning_numbers, our_numbers = [x.split(" ") for x in line[start_of_line:-1].split("|")]
            overlap = len({x for x in winning_numbers if x != ""} & {x for x in our_numbers if x != ""}) #set intersection
            if overlap:
                running_total += 2 ** (overlap - 1) #score doubles each overlap starting at 1 ie 2^(overlap-1)
    return running_total

EXAMPLE_SOLUTION = 13
if (test_solution := card_reader("example") == EXAMPLE_SOLUTION):
    print("passed test!")
    print("solution should be {}".format(card_reader("input")))
