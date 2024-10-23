import math

def parseInput(path):
    with open(path) as rawtxt:
        workingarray = []

        for line in rawtxt:
            line = line.strip()
            timeOrDistance = [int(x) for x in line.split(" ") if x.isnumeric()]
            workingarray.append(timeOrDistance)

    output = [{"time": time, "distance" : distance} for time, distance in zip(workingarray[0],workingarray[1])]
    return output

def solveInput(timeDistancePairs: list[dict[int:int]]):
    numWins = []
    for pair in timeDistancePairs:
        numWins.append(solveRace(pair["time"], pair["distance"]))
    return math.prod(numWins)

def solveRace(time: int, distance: int):
    for k in range(time + 1):
        distance_travelled = k * (time - k)
        if distance_travelled > distance:
            failed_attempts = k
            return time + 1 - (2 * failed_attempts)
    
def parseInput2(path):
    with open(path) as rawtxt:
        workingarray = []

        for line in rawtxt:
            line_pieces = ""
            for c in line:
                if c.isnumeric():
                    line_pieces += c
            workingarray.append([int(line_pieces)])

    output = [{"time": time, "distance" : distance} for time, distance in zip(workingarray[0],workingarray[1])]
    return output