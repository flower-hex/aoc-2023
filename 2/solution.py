COLOUR_MAXIMUMS = {"red" : 12,
                   "green" : 13,
                   "blue" : 14}

PART_TWO = True

def bag_looker(filename):
    with open(filename) as rawtxt:
        solution_sum = 0
        game_count = 0
        for line in rawtxt:
            game_count += 1
            line_start = line.index(":") + 1
            reveals = line[line_start:-1].split(";")
            if not PART_TWO:
                if cubes_possibility_check(reveals):
                    solution_sum += game_count
            else:
                solution_sum += cubes_possibility_constrainer(reveals)
    return solution_sum

def cubes_possibility_check(reveals): #part 1
    for reveal in reveals:
        cube_reveals = reveal.split(",")
        for cube in cube_reveals:
            cube_value, cube_colour = cube[1:].split(" ")
            if int(cube_value) > COLOUR_MAXIMUMS[cube_colour]:
                #print("{} exceeded colour maximum of {}".format(cube_value, COLOUR_MAXIMUMS[cube_colour]))
                return False
    return True

def cubes_possibility_constrainer(reveals): #part 2
    colour_min_values = {"red" : 0,
                         "green" : 0,
                         "blue" : 0}
    for reveal in reveals:
        cube_reveals = reveal.split(",")
        for cube in cube_reveals:
            cube_value, cube_colour = cube[1:].split(" ")
            if int(cube_value) > colour_min_values[cube_colour]:
                colour_min_values[cube_colour] = int(cube_value)
    return colour_min_values["red"] * colour_min_values["green"] * colour_min_values["blue"]


if not PART_TWO:
    if (test := bag_looker("example")) == 8: #known example test
        print("passed test!")
        print("\nSolution should be {}".format(bag_looker("input")))
    else:
        print("failed test with result {}, should be 8".format(test))

else:
    if (test := bag_looker("example")) == 2286: #known example test
        print("passed test!")
        print("\nSolution should be {}".format(bag_looker("input")))
