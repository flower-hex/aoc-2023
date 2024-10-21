import solution

finalInput = solution.parseInput("input.txt")
finalResult = solution.solveInput(finalInput)
print("part 1: {}".format(finalResult))

finalInput2 = solution.parseInput2("input.txt")
finalResult2 = solution.solveInput(finalInput2)
print("part 2: {}".format(finalResult2))