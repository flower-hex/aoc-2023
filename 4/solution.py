def card_reader(filename):
    with open(filename) as rawtxt:
        running_total = 0
        card_index = -1
        card_rolodex = []
        for line in rawtxt:
            card_rolodex.append(0) #populate rolodex quickly
        rawtxt.seek(0) #reset to start of file
        for line in rawtxt:
            card_index += 1
            card_rolodex[card_index] += 1
            start_of_line = line.index(":") + 1
            winning_numbers, our_numbers = [x.split(" ") for x in line[start_of_line:-1].split("|")]
            overlap = len({x for x in winning_numbers if x != ""} & {x for x in our_numbers if x != ""}) #set intersection
            if overlap:
                for i in range(1, overlap + 1):
                    card_rolodex[card_index + i] += 1 * card_rolodex[card_index]
    return sum(card_rolodex)

PART2 = True
if not PART2:
    EXAMPLE_SOLUTION = 13
else:
    EXAMPLE_SOLUTION = 30
if (test_solution := card_reader("example") == EXAMPLE_SOLUTION):
    print("passed test!")
    print("solution should be {}".format(card_reader("input")))
