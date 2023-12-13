def almanac_interpreter(filename):
    with open(filename) as rawtxt:
        seeds = []
        seeds_mapped = []
        mapped_seeds_for_deletion = []
        for line in rawtxt:
            if "seeds: " in line:
                seeds = line[line.index(":")+2:-1].split(" ")
                seeds = [int(x) for x in seeds]
                #seeds = [seeds[3]] # for testing
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
    return min(seeds)

def create_mapping(mapping, x):
    return

EXAMPLE_SOLUTION = 35
if (solution := almanac_interpreter("example")) == EXAMPLE_SOLUTION:
    print("passed test!")
    print("solution should be {}".format(almanac_interpreter("input")))
else:
    print(f"failed test with result {solution}")
