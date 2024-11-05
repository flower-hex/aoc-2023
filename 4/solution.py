def card_reader(filename):
    with open(filename) as rawtxt:
        card_index = -1
        card_rolodex = []
        for line in rawtxt:
            card_rolodex.append(1) #populate rolodex quickly
        rawtxt.seek(0) #reset to start of file
        for line in rawtxt:
            card_index += 1
            start_of_line = line.index(":") + 1
            winning_numbers, our_numbers = [x.split(" ") for x in line[start_of_line:-1].split("|")] #get a pair of lists of numbers for the current card
            overlap = len({x for x in winning_numbers if x != ""} & {x for x in our_numbers}) #set intersection
            if overlap:
                for i in range(1, overlap + 1):
                    card_rolodex[card_index + i] += card_rolodex[card_index] #increment future cards for each copy of the current card
    return sum(card_rolodex)

EXAMPLE_SOLUTION = 30
if (test_solution := card_reader("example") == EXAMPLE_SOLUTION):
    print("passed test!")
    print("solution should be {}".format(card_reader("input")))
