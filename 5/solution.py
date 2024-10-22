PART_1 = True
NOISY = False
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
    if NOISY: print("full list of mappings: {}".format(mappings))
    return seeds, mappings

# def apply_mappings(value, mappings):
#     for i in range(len(mappings)-1):
#         if (mappings[i][0] <= value < mappings[i+1][0]): # 'mappings[i][0] <=' is redundant for ordered list
#             return value + mappings[i][1]
#     return value + mappings[-1][1]
#
# def reverse_mappings(value, mappings):
#     for i in range(len(mappings)-1):
#         if (mappings[i][0] <= value < mappings[i+1][0]): # 'mappings[i][0] <=' is redundant for ordered list
#             return value - mappings[i][1]
#     return value - mappings[-1][1]

def mapping_consolidator(mappings):
    mappings = [mappings[-i-1] for i in range(len(mappings))]
    consolidated_mappings = []
    for new_layer in mappings:
        old_consolidated_layer = [x + [] for x in consolidated_mappings] # deepcopy
        new_consolidated_layer = []
        for new_mapping in new_layer:
            adjustment = new_mapping["destination start"] - new_mapping["source start"]
            upper_bound = new_mapping["source start"] + new_mapping["range length"]
            lower_bound = new_mapping["source start"]
            for i in range(len(old_consolidated_layer)):
                if lower_bound <= old_consolidated_layer[i][0] - adjustment < upper_bound: #-adjustment because we're going backwards
                    if NOISY: print("found old mapping {} in new mapping {}, moving to [{},{}]".format(old_consolidated_layer[i], new_mapping,old_consolidated_layer[i][0] - adjustment, adjustment + old_consolidated_layer[i][1]))
                    new_consolidated_layer.append([old_consolidated_layer[i][0] - adjustment, adjustment + old_consolidated_layer[i][1]]) # the adjustments are summed together so that the output remains the same
                if i < len(old_consolidated_layer) -1 and upper_bound in range(old_consolidated_layer[i][0],old_consolidated_layer[i+1][0]):
                    if NOISY: print("found upper bound {} in {}, moving to [{},{}]".format(upper_bound,range(old_consolidated_layer[i][0],old_consolidated_layer[i+1][0]),upper_bound, old_consolidated_layer[i][1]))
                    if upper_bound not in [x[0] for x in new_consolidated_layer]:
                        new_consolidated_layer.append([upper_bound, old_consolidated_layer[i][1]])
            for wip_new_mapping in new_consolidated_layer:
                if lower_bound == wip_new_mapping[0]: #e.g. if one new range starts where another ended
                    wip_new_mapping[1] = wip_new_mapping[1] + adjustment
                    break
            else:
                if len(consolidated_mappings) == 0 or new_mapping["destination start"] < consolidated_mappings[0][0]:
                    new_consolidated_layer.append([lower_bound, adjustment])
                elif consolidated_mappings[-1][0] < new_mapping["destination start"]:
                    new_consolidated_layer.append([lower_bound, adjustment + consolidated_mappings[-1][1]])
                else:
                    for i in range(len(consolidated_mappings) -1): #this should be sorted ascending
                        if new_mapping["destination start"] < consolidated_mappings[i+1][0]:
                            new_consolidated_layer.append([lower_bound, adjustment + consolidated_mappings[i][1]])
                            break
                    else: #if for loop doesn't break
                        input("couldn't place new mapping lower bound {}".format(lower_bound))
            for wip_new_mapping in new_consolidated_layer:
                if upper_bound == wip_new_mapping[0]:
                    break
            else:
                new_consolidated_layer.append([upper_bound, 0])
        new_consolidated_layer.sort()
        consolidated_mappings = []
        for old_mapping in old_consolidated_layer:
            for i in range(len(new_consolidated_layer) - 1):
                if old_mapping[0] < new_consolidated_layer[i+1][0] and new_consolidated_layer[i][1] == 0:
                    consolidated_mappings.append(old_mapping)
                    break
            else:
                if old_mapping[0] > new_consolidated_layer[-1][0] or old_mapping[0] < new_consolidated_layer[0][0]:
                    if NOISY: print("inserting old mapping {} as either > {} or < {}".format(old_mapping[0], new_consolidated_layer[-1][0], new_consolidated_layer[0][0]))
                    consolidated_mappings.append(old_mapping)
        consolidated_mappings += new_consolidated_layer
        consolidated_mappings.sort()
    return consolidated_mappings

def almanac_solver(filename):
    seeds, mappings = almanac_interpreter(filename) #get seeds in form of ranges and mappings in form of list of lists of dictionaries
    mappings = mapping_consolidator(mappings)
    print(mappings)
    solutions = []
    for seed in seeds:
        if seed < mappings[0][0]:
            solutions.append(seed + mappings[0][1])
            if NOISY: print("{} became {}".format(seed, seed + mappings[0][1]))
        elif seed > mappings[-1][0]:
            solutions.append(seed + mappings[-1][1])
            if NOISY: print("{} became {}".format(seed, seed + mappings[-1][1]))
        else:
            for i in range(len(mappings)-1):
                if seed < mappings[i+1][0]:
                    solutions.append(seed + mappings[i][1])
                    if NOISY: print("{} became {}".format(seed, seed + mappings[i][1]))
                    break
    return min(solutions)
    ##former part 2 solution##
    # for possible_solution in range(10000000): #starting at 0, test end points to see if they're reachable from a valid seed
    #     possible_solution_copy = possible_solution
    #     for i in range(1, len(mappings)+1):
    #         for mapping in mappings[-i]: #work backwards through the mappings
    #             if possible_solution in range(mapping["destination start"], mapping["destination start"] + mapping["range length"]):
    #                 possible_solution -= mapping["destination start"] - mapping["source start"]
    #                 break #if one mapping is applicable, don't apply any others from this group
    #     for seed in seeds:
    #         if possible_solution in seed: #seed is a range
    #             return possible_solution_copy
    # print("reached end of range without finding solution")
    # return -1

if (solution := almanac_solver("example")) == EXAMPLE_SOLUTION:
    input(f"passed test with solution {solution}!")
    print("solution should be {}".format(almanac_solver("input")))
else:
    print(f"failed test with result {solution}")
