def bag_looker(filename):
    with open(filename) as rawtxt:
        solution_sum = 0
        game_count = 0
        for line in rawtxt:
            game_count += 1
            line_start = line.index(":") + 1
            reveals = line[line_start:-1].split(";")
            solution_sum += cubes_possibility_constrainer(reveals)
    return solution_sum

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

if (test := bag_looker("example")) == 2286: #known example test
    print("passed test!")
    print("\nSolution should be {}".format(bag_looker("input")))
else:
    print("failed test with result {}, should be 2286".format(test))
