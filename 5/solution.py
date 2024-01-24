PART_1 = True
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
    #print(mappings)
    return seeds, mappings

def apply_mappings(value, mappings):
    for i in range(len(mappings)-1):
        if (mappings[i][0] <= value < mappings[i+1][0]): # 'mappings[i][0] <=' is redundant for ordered list
            return value + mappings[i][1]
    return value + mappings[-1][1]

def reverse_mappings(value, mappings):
    for i in range(len(mappings)-1):
        if (mappings[i][0] <= value < mappings[i+1][0]): # 'mappings[i][0] <=' is redundant for ordered list
            return value - mappings[i][1]
    return value - mappings[-1][1]

def mapping_consolidator(mappings):
    # consolidated_mappings = [] # dictionaries of "range", "adjustment" (int)
    # for category in mappings:
    #     for mapping in category:
    #         new_range = range(mapping["source start"], mapping["source start"] + mapping["range length"])
    #         new_adjustment_value = mapping["source start"] - mapping["source destination"]
    #         for i in range(len(consolidated_mappings)):
    #             if mapping["source start"] in consolidated_mappings[i]["range"]:
    #                 if
    #
    #             if mapping["source start"] + mapping["range length"] in existing_mapping[0]

    # create list of tuples (range start, adjustment)

    # find x = largest item[0] in list which is < lower bound (default to 0)
    # new item in list is (lower bound, adjustment + x[1])

    # for each item in list, see if item[0] in new range
    # if so, keep track of new value y = item[1] if this is the largest item[0] found (this value defaults to 0) and adjust value appropriately (item[1] += new[1])
    # once compared against everything, set upper bound as new item in list (upper bound, y) unless this item already exists





    # consolidated_mappings = [[0,0]]
    #
    # mappings = [mappings[-i-1] for i in range(len(mappings))]
    # for x in mappings:
    #     print(x)
    # for category in mappings:
    #     consolidated_mappings_old = [x + [] for x in consolidated_mappings] #deepcopy so it doesn't just do references
    #     consolidated_mappings_old.sort()
    #     print("new")
    #     for mapping in category:
    #         adjustment = mapping["source start"] - mapping["destination start"]
    #         upper_bound = reverse_mappings(mapping["destination start"] + mapping["range length"], consolidated_mappings_old)
    #         lower_bound = reverse_mappings(mapping["destination start"], consolidated_mappings_old)
    #         print("{} becomes {}".format(mapping["destination start"], lower_bound))
    #         x = 0,0
    #         y = 0,0
    #         #x = max([item for item in consolidated_mappings if item[0] < mapping["source start"]]):
    #         for item in consolidated_mappings:
    #             if item[0] < lower_bound and item[0] >= x[0]:
    #                 x = item + []
    #             if lower_bound <= item[0] < upper_bound:
    #                 if item[0] > y[0]:
    #                     y = item + []
    #                 item[1] += adjustment
    #
    #         for item in consolidated_mappings:
    #             if item[0] == lower_bound:
    #                 item = lower_bound, adjustment + x[1]
    #                 break
    #         else:
    #             consolidated_mappings.append([lower_bound, adjustment + x[1]])
    #
    #         for item in consolidated_mappings:
    #             if item[0] == upper_bound:
    #                 item = [upper_bound, y[1]]
    #                 break
    #         else:
    #             consolidated_mappings.append([upper_bound, y[1]])
    #
    #     print(sorted(consolidated_mappings))
    #     print()

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
                    #print("found old mapping {} in new mapping {}, moving to [{},{}]".format(old_consolidated_layer[i], new_mapping,old_consolidated_layer[i][0] - adjustment, adjustment + old_consolidated_layer[i][1]))
                    new_consolidated_layer.append([old_consolidated_layer[i][0] - adjustment, adjustment + old_consolidated_layer[i][1]]) # the adjustments are summed together so that the output remains the same
                if i < len(old_consolidated_layer) -1 and upper_bound in range(old_consolidated_layer[i][0],old_consolidated_layer[i+1][0]):
                    #print("found upper bound {} in {}, moving to [{},{}]".format(upper_bound,range(old_consolidated_layer[i][0],old_consolidated_layer[i+1][0]),upper_bound, old_consolidated_layer[i][1]))
                    if upper_bound not in [x[0] for x in new_consolidated_layer]:
                        new_consolidated_layer.append([upper_bound, old_consolidated_layer[i][1]]) #+adjustment because we're applying an adjustment forwards to create a new lower bound for a range from a layer applied subsequently to this one (and processed previously)
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
            print(new_consolidated_layer)
        new_consolidated_layer.sort()
        consolidated_mappings = []
        for old_mapping in old_consolidated_layer:
            for i in range(len(new_consolidated_layer) - 1):
                if old_mapping[0] < new_consolidated_layer[i+1][0] and new_consolidated_layer[i][1] == 0:
                    consolidated_mappings.append(old_mapping)
                    print("don't think this is relevant")
                    break
            else:
                if old_mapping[0] > new_consolidated_layer[-1][0] or old_mapping[0] < new_consolidated_layer[0][0]:
                    print("inserting old mapping {0} as either > {1} or < {2}".format(old_mapping[0], new_consolidated_layer[-1][0], new_consolidated_layer[0][0]))
                    consolidated_mappings.append(old_mapping)
        consolidated_mappings += new_consolidated_layer
        print()
        consolidated_mappings.sort()
        print(consolidated_mappings)
        print()
    return consolidated_mappings

def almanac_solver(filename):
    seeds, mappings = almanac_interpreter(filename) #get seeds in form of ranges and mappings in form of list of lists of dictionaries
    mappings = mapping_consolidator(mappings)
    #return -1
    print(seeds)
    print(mappings)
    solutions = []
    for seed in seeds:
        if seed < mappings[0][0]:
            solutions.append(seed + mappings[0][1])
            print("{} became {}".format(seed, seed + mappings[0][1]))
        elif seed > mappings[-1][0]:
            solutions.append(seed + mappings[-1][1])
            print("{} became {}".format(seed, seed + mappings[-1][1]))
        else:
            for i in range(len(mappings)-1):
                if seed < mappings[i+1][0]:
                    solutions.append(seed + mappings[i][1])
                    print("{} became {}".format(seed, seed + mappings[i][1]))
                    break
    return min(solutions)
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
    print(f"passed test with solution {solution}!")
    print("solution should be {}".format(almanac_solver("input")))
else:
    print(f"failed test with result {solution}")
