import math

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
# # part 1
# solution = traverseNetwork(directions, network, STARTPOINT, ENDPOINT)
# print("day 8 solution is {}".format(solution))

def findStartEndPoints(network):
    # create sets for our part 2 start and end points
    startpoints = set()
    endpoints = set()
    nodes = network.keys()
    for node in nodes:
        if node[-1] == "A": # if last letter is A
            startpoints |= {node}
        elif node[-1] == "Z":
            endpoints |= {node}
    return (startpoints, endpoints)

startpoints_part2, endpoints_part2 = findStartEndPoints(network)
# solution_part2 = traverseNetwork(directions, network, start_part2, end_part2)
# print("day 8 part 2 solution is {}".format(solution_part2))

def traverseNetworkRecordingWeights(directions, network, start_id : tuple[str|int], endpoints):
    currentNode, directions_index = start_id
    explored_nodes = []

    while len(explored_nodes) < 100000: # timeout if it takes too many tries to solve
        for i in range(directions_index,len(directions)):
            instruction = directions[i]
            explored_nodes.append((currentNode,i)) # this is the node + instruction index identifier
            currentNode = network[currentNode][instruction]
            if currentNode in endpoints:

                steps = len(explored_nodes)
                # fold the numberline in backwards over the explored nodes to add the step counts
                # i.e.  n,          n-1,   n-2   ... 2,      1       (not recorded)
                #       startpoint, id[1], id[2] ... id[-2], id[-1], endpoint
                explored_nodes = {a : (b, currentNode) for a,b in zip(explored_nodes, range(steps,0,-1))}

                end_id = (currentNode, steps % len(directions)) # steps modulo len(directions) to get final position in directions

                return explored_nodes, end_id
        
        directions_index = 0 # reset directions start point before looping over it
    
    print("could not find path through network - too many tries")

def build_solved_network():
    weighted_graph = {}
    for startpoint in startpoints_part2:
        point_id = (startpoint, 0)
        while point_id not in weighted_graph:
            graph_additions, point_id = traverseNetworkRecordingWeights(directions,network,point_id,endpoints_part2)
            weighted_graph |= graph_additions
    return weighted_graph

# # testing the weighted graph
# solved_network = build_solved_network()
# for startpoint in startpoints_part2:
#     steps, endpoint = solved_network[startpoint, 0]
#     offset = steps % len(directions)
#     print("starting from point {startpoint} with an initial offset of {startoffset} we are {steps} steps away from endpoint {endpoint}, which we will arrive at with an offset of {offset}".format(startpoint=startpoint, startoffset=0,steps=steps, endpoint=endpoint, offset=offset))
#     startoffset = offset
#     steps, endpoint = solved_network[endpoint, offset]
#     offset = steps % len(directions)
#     print("starting from point {startpoint} with an initial offset of {startoffset} we are {steps} steps away from endpoint {endpoint}, which we will arrive at with an offset of {offset}".format(startpoint=endpoint, startoffset=startoffset,steps=steps, endpoint=endpoint, offset=offset))
# 
# ok well it turns out for my input the endpoints are always arrived at on a perfect multiple of the length of the instructions, and they always loop back to their start point immediately
# so the problem is trivial and i could've solved it with a pen and paper
# not sure if there was some way to know the input would conform to that pattern or if it always does, it wasn't specified in the instructions
# this solution is much more resilient to more varied inputs but excessive for the input i was given

# quick and easy solution with this new knowledge which does not use 99% of the working out above
solved_network = build_solved_network()
step_counts = [a for a, b in [solved_network[x, 0] for x in startpoints_part2]]
print(math.lcm(*step_counts))