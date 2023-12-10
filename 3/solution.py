def schematic_reader(filename):
    with open(filename) as rawtxt:
        schematic = []
        for line in rawtxt:
            schematic.append([])
            for c in line.strip():
                schematic[-1].append(c)
    # for line in schematic:
    #     print(line)
    return schematic

def symbol_finder(schematic):
    symbol_locations = []
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if (schematic[y][x] not in "0123456789." and not PART_TWO) or (PART_TWO and schematic[y][x] == "*"):
                symbol_locations.append({"y" : y, "x" : x})
    return symbol_locations

def schematic_solver(filename):
    schematic = schematic_reader(filename)
    symbol_locations = symbol_finder(schematic)
    gear_adjacencies = []
    solution = 0
    for y in range(len(schematic)):
        current_num = ""
        current_num_gear_coords = {}
        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                current_num += schematic[y][x]
                for symbol in symbol_locations:
                    if abs(symbol["y"] - y) <= 1 and abs(symbol["x"] - x) <= 1: #check for adjacent symbol x+-1, y+-1
                        #print("matched symbol {} with point y={}x={}".format(symbol, y, x))
                        current_num_gear_coords = {"y" : symbol["y"], "x" : symbol["x"]}
                        break
            if not schematic[y][x].isdigit() and current_num != "":
                if current_num_gear_coords != {}:
                    gear_adjacencies.append({"number" : current_num, "gear" : current_num_gear_coords})
                #reset number
                current_num = ""
                current_num_gear_coords = {}
        if current_num_gear_coords != {}:
            gear_adjacencies.append({"number" : current_num, "gear" : current_num_gear_coords})
    for adjacency_a in gear_adjacencies:
        #gear_adjacencies.pop(0)
        gear_engaged = False
        for adjacency_b in gear_adjacencies:
            if adjacency_a == adjacency_b:
                continue
            if adjacency_a["gear"] == adjacency_b["gear"]:
                if gear_engaged:
                    break
                gear_engaged = True
                #print("gear engaged for first time at {} ({}) by {} and {}".format(adjacency_a["gear"], adjacency_b["gear"], adjacency_a["number"], adjacency_b["number"]))
                secondary_value = adjacency_b["number"]
        if gear_engaged:
            solution += int(adjacency_a["number"]) * int(secondary_value)
    return solution / 2

def schematic_solver_part_one(filename):
    schematic = schematic_reader(filename)
    symbol_locations = symbol_finder(schematic)
    gear_ratio = 0
    for y in range(len(schematic)):
        current_num = ""
        current_num_has_gear = False
        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                current_num += schematic[y][x]
                for symbol in symbol_locations:
                    if abs(symbol["y"] - y) <= 1 and abs(symbol["x"] - x) <= 1: #check for adjacent symbol x+-1, y+-1
                        #print("matched symbol {} with point y={}x={}".format(symbol, y, x))
                        current_num_has_symbol = True
                        break
            if not schematic[y][x].isdigit() and current_num != "":
                if current_num_has_symbol:
                    part_number_sum += int(current_num)
                #reset number
                current_num = ""
                current_num_has_symbol = False
        if current_num_has_symbol:
                part_number_sum += int(current_num)
    return part_number_sum

#test
PART_TWO = True
if not PART_TWO:
    EXAMPLE_SOLUTION = 4361
else:
    EXAMPLE_SOLUTION = 467835
if (possible_solution := schematic_solver("example")) == EXAMPLE_SOLUTION:
    print("\npassed test\n")
    print("solution should be {}".format(schematic_solver("input")))
else:
    print("failed test with result {}, should be {}".format(possible_solution, EXAMPLE_SOLUTION))
