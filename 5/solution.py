PART_1 = False
if PART_1:
    EXAMPLE_SOLUTION = 35
else:
    EXAMPLE_SOLUTION = 46

def almanac_interpreter(filename):
    with open(filename) as rawtxt:
        seeds = []
        mappings = []
        for line in rawtxt:
            if "seeds: " in line:
                seeds = line[line.index(":")+2:-1].split(" ")
                seeds = [int(x) for x in seeds]
                if not PART_1:
                    seeds_temp = []
                    for i in range(len(seeds)):
                        if i % 2 == 0:
                            seeds_temp += [range(seeds[i], seeds[i] + seeds[i+1])]
                    seeds = seeds_temp
            elif ":" in line:
                mappings.append([])
            elif line[0].isdigit():
                new_mapping = line[:-1].split(" ")
                new_mapping = dict(zip(["destination start", "source start", "range length"], [int(x) for x in new_mapping]))
                mappings[-1].append(new_mapping)
    print(mappings)
    return seeds, mappings

def almanac_solver(filename):
    seeds, mappings = almanac_interpreter(filename) #get seeds in form of ranges and mappings in form of list of lists of dictionaries
    for possible_solution in range(10000000): #starting at 0, test end points to see if they're reachable from a valid seed
        possible_solution_copy = possible_solution
        for i in range(1, len(mappings)+1):
            for mapping in mappings[-i]: #work backwards through the mappings
                if possible_solution in range(mapping["destination start"], mapping["destination start"] + mapping["range length"]):
                    possible_solution -= mapping["destination start"] - mapping["source start"]
                    break #if one mapping is applicable, don't apply any others
        for seed in seeds:
            if possible_solution in seed: #seed is a range
                return possible_solution_copy
    print("reached end of range without finding solution")
    return -1

if (solution := almanac_solver("example")) == EXAMPLE_SOLUTION:
    print(f"passed test with solution {solution}!")
    print("solution should be {}".format(almanac_solver("input")))
else:
    print(f"failed test with result {solution}")
