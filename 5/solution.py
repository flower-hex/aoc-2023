PART_1 = False
if PART_1:
    EXAMPLE_SOLUTION = 35
else:
    EXAMPLE_SOLUTION = 46

def almanac_interpreter(filename):
    with open(filename) as rawtxt:
        seeds = []
        seeds_mapped = []
        mapped_seeds_for_deletion = []
        for line in rawtxt:
            print(seeds)
            if "seeds: " in line:
                seeds = line[line.index(":")+2:-1].split(" ")
                seeds = [int(x) for x in seeds]
                if not PART_1:
                    for i in range(len(seeds)):
                        if i % 2 == 0:
                            seeds_mapped += [x for x in range(seeds[i], seeds[i] + seeds[i+1])]
                    seeds = []
            elif ":" in line:
                seeds += seeds_mapped
                seeds_mapped = []
            elif line[0].isdigit():
                mapping = line[:-1].split(" ")
                mapping = dict(zip(["destination start", "source start", "range length"], [int(x) for x in mapping]))
                for seed in seeds:
                    if seed in range(mapping["source start"], mapping["source start"] + mapping["range length"]):
                        #print("{seed} in range starting {start} and ending {end}".format(seed=seed, start=mapping["source start"], end=mapping["range length"]))
                        seeds_mapped.append(mapping["destination start"] + seed - mapping["source start"])
                        mapped_seeds_for_deletion.append(seed)
                seeds = [x for x in seeds if x not in mapped_seeds_for_deletion]
                mapped_seeds_for_deletion = []
    seeds += seeds_mapped
    print(seeds)
    return min(seeds)

if (solution := almanac_interpreter("example")) == EXAMPLE_SOLUTION:
    print(f"passed test with solution {solution}!")
    print("solution should be {}".format(almanac_interpreter("input")))
else:
    print(f"failed test with result {solution}")
