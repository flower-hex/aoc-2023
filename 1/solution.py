number_keys = {"one" : "1",
              "two" : "2",
              "three" : "3",
              "four" : "4",
              "five" : "5",
              "six" : "6",
              "seven" : "7",
              "eight" : "8",
              "nine" : "9",
              "1" : "1",
              "2" : "2",
              "3" : "3",
              "4" : "4",
              "5" : "5",
              "6" : "6",
              "7" : "7",
              "8" : "8",
              "9" : "9"}

def calibrator(filename):
    running_total = 0
    with open(filename) as rawtxt:
        for line in rawtxt:
            furthest_position = -1
            nearest_position = float('inf')
            for num in number_keys: #check each possible digit and compare its index to find highest and lowest index
                l_position = line.find(num)
                if l_position == -1: continue #not in line
                r_position = line.rfind(num) #highest index
                if l_position < nearest_position:
                    nearest_position = l_position
                    line_value = number_keys[num]
                if r_position > furthest_position:
                    furthest_position = r_position
                    line_value2 = number_keys[num]
            running_total += int(line_value + line_value2)
    return running_total

#test
example2_solution = calibrator("example2")
if example2_solution == 281: #known solution
    print("passed test!\nsolution should be " + str(calibrator("input")))
else:
    print("failed test, returned: " + str(example2_solution))
