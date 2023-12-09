COLOUR_MAXIMUMS = {"red" : 12,
                   "green" : 13,
                   "blue" : 14}

def bag_looker(filename):
    with open(filename) as rawtxt:
        game_id_sum = 0
        game_count = 0
        for line in rawtxt:
            game_count += 1
            line_start = line.index(":") + 1
            reveals = line[line_start:-1].split(";")
            if cubes_possibility_check(reveals):
                game_id_sum += game_count
    return game_id_sum

def cubes_possibility_check(reveals):
    for reveal in reveals:
        cube_reveals = reveal.split(",")
        for cube in cube_reveals:
            print(cube)
            cube_value, cube_colour = cube[1:].split(" ")
            if int(cube_value) > COLOUR_MAXIMUMS[cube_colour]:
                #print("{} exceeded colour maximum of {}".format(cube_value, COLOUR_MAXIMUMS[cube_colour]))
                return False
    return True

if (test := bag_looker("example")) == 8: #known example test
    print("passed test!")
    print("/nSolution should be {}".format(bag_looker("input")))
else:
    print("failed test with result {}, should be 8".format(test))
