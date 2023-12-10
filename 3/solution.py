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
            if schematic[y][x] not in "0123456789.":
                symbol_locations.append({"y" : y, "x" : x})
    return symbol_locations

def schematic_solver(filename):
    schematic = schematic_reader(filename)
    symbol_locations = symbol_finder(schematic)
    part_number_sum = 0
    for y in range(len(schematic)):
        current_num = ""
        current_num_has_symbol = False
        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                current_num += schematic[y][x]
                for symbol in symbol_locations:
                    if abs(symbol["y"] - y) <= 1 and abs(symbol["x"] - x) <= 1:
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
EXAMPLE_SOLUTION = 4361
if (possible_solution := schematic_solver("example")) == EXAMPLE_SOLUTION:
    print("\npassed test\n")
    print("solution should be {}".format(schematic_solver("input")))
else:
    print("failed test with result {}, should be {}".format(possible_solution, EXAMPLE_SOLUTION))
