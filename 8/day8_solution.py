STARTPOINT = "AAA"
ENDPOINT = "ZZZ"
INPUT_PATH = "8/input.txt"

def parseInput(path):
    with open(path) as rawtxt:
        directions = []
        network = {}
        for c in rawtxt.readline():
            if c == "L":
                directions.append(0)
            elif c == "R":
                directions.append(1)
        for line in rawtxt:
            if "=" in line:
                key, value = line.split(" = ")
                value = value.strip("()\n")
                values = tuple(value.split(", "))
                node = {key : values}
                network |= node
        return (directions, network)
    
def traverseNetwork(directions, network, startpoint, endpoint):
    currentNode = startpoint
    steps = 0
    while currentNode != endpoint:
        for instruction in directions:
            currentNode = network[currentNode][instruction]
            steps += 1
    return steps

directions, network = parseInput(INPUT_PATH)
solution = traverseNetwork(directions, network, STARTPOINT, ENDPOINT)
print("day 8 solution is {}".format(solution))