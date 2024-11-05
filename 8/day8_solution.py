STARTPOINT = {"AAA"}
ENDPOINT = {"ZZZ"}
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
    
def traverseNetwork(directions, network, startpoints, endpoints):
    currentNodes = startpoints
    steps = 0
    while not (currentNodes <= endpoints): # while not every current node is in endpoints
        for instruction in directions:
            currentNodes = {network[node][instruction] for node in currentNodes}
            steps += 1 # for each instruction we take one step and update each current node
            if steps == 1000000:
                return "too many loops"
    return steps

directions, network = parseInput(INPUT_PATH)
solution = traverseNetwork(directions, network, STARTPOINT, ENDPOINT)
print("day 8 solution is {}".format(solution))

def findStartEndPoints(network):
    startpoints = set()
    endpoints = set()
    nodes = network.keys()
    for node in nodes:
        if node[-1] == "A": # if last letter is A
            startpoints |= {node}
        elif node[-1] == "Z":
            endpoints |= {node}
    return (startpoints, endpoints)

start_part2, end_part2 = findStartEndPoints(network)
solution_part2 = traverseNetwork(directions, network, start_part2, end_part2)
print("day 8 part 2 solution is {}".format(solution_part2))

# def traverseNetworkRewrite(directions : list[bool],
#                            network : set[str:tuple],
#                            currentNodes : set[str],
#                            endpoints : set[str]):
#     node = currentNodes.pop()
#     for instruction in directions:
#         steps += 1
#         node = network[node][instruction]
#         if node in endpoints:
#             for node in currentNodes:
#                 for instruction in directions:
#                     node = network[node][instruction]
#                     if node in endpoints:

def solveNetwork(directions, network):
# create a weighted graph with number of steps to an end point for each node for each direction index point

    instructionIndex = int()
    nearestEndpointCount = int()
    nearestEndpointId = str()
    edge_solution = tuple( nearestEndpointCount, nearestEndpointId )
    nodeID = str()
    solvedGraph = set( nodeID : set( instructionIndex : edge_solution ))

    for start in directions:
        
