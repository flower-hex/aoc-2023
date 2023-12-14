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
                            seeds_temp += [x for x in range(seeds[i], seeds[i] + seeds[i+1])]
                    seeds = seeds_temp
                    print(seeds)
            elif ":" in line:
                mappings.append([])
            elif line[0].isdigit():
                new_mapping = line[:-1].split(" ")
                new_mapping = dict(zip(["destination start", "source start", "range length"], [int(x) for x in new_mapping]))
                mappings[-1].append(new_mapping)
    print(mappings)
    return min(seeds)

if (solution := almanac_interpreter("example")) == EXAMPLE_SOLUTION:
    print(f"passed test with solution {solution}!")
    input()
    print("solution should be {}".format(almanac_interpreter("input")))
else:
    print(f"failed test with result {solution}")
