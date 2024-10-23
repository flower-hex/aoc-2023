def parseInput(path : str):
    with open(path) as rawtxt:
        hands = []

        for line in rawtxt:
            a, b = line.split()
            formattedline = {"cards" : a, "bid" : int(b)}
            hands.append(formattedline)

        return hands
    
def sortHands(hands : list[dict["cards" : str, "bid" : int]], isPart2 : bool = 0):

    handTypes = []
    for _ in range(7): # 7 types of hands (see below)
        handTypes.append([])

    #enum style hand names for clarity - ordered lowest to highest
    highCard = 0        # 23456
    pair = 1            # A23A4
    twoPair = 2         # 23432
    threeOfAKind = 3    # TTT98
    fullHouse = 4       # 23332
    fourOfAKind = 5     # AA8AA
    fiveOfAKind = 6     # AAAAA
    
    for hand in hands:
        if isPart2 and "J" in hand["cards"]:
            handMinusJ = set(c for c in hand["cards"]) - {"J"}
            quickCount = len(handMinusJ)

            if quickCount <= 1: #aJJJJ or JJJJJ
                handID = fiveOfAKind

            elif quickCount == 2: # aabbJ or aabJJ or abJJJ, aabbJ = fullhouse
                if hand["cards"].count(handMinusJ.pop()) == 2 and hand["cards"].count(handMinusJ.pop()) == 2:
                    handID = fullHouse
                else:
                    handID = fourOfAKind
            
            elif quickCount == 3: # abcJJ or aabcJ
                handID = threeOfAKind
            
            else: # abcdJ
                handID = pair

        else:
            # start by sorting the hand into its type by using the number of character repeats
            quickCount = len(set(c for c in hand["cards"]))

            if quickCount == 5: # 5 different cards
                handID = highCard
                
            elif quickCount == 4: # 4 different
                handID = pair

            elif quickCount == 1: # ding ding ding
                handID = fiveOfAKind

            elif quickCount == 2: # four of a kind OR full house
                if hand["cards"].count(hand["cards"][0]) in (1,4):
                    handID = fourOfAKind
                else:
                    handID = fullHouse

            else: # three of a kind OR two pair
                assert quickCount == 3
                for c in hand["cards"]: # first card 
                    cardCount = hand["cards"].count(c)
                    if cardCount == 2:
                        handID = twoPair
                        break
                    elif cardCount == 3:
                        handID = threeOfAKind
                        break

        handTypes[handID] = sortHandsWithinTypes(handTypes[handID], hand, isPart2)

    return handTypes


def newHandLessThanOldHand(oldHand, newHand, isPart2 : bool = 0):
    cardValues = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    if isPart2:
        cardValues = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    for i in range(5): # 5 cards per hand
        oldCard = oldHand["cards"][i] # ith card of old hand
        newCard = newHand["cards"][i]
        for c in cardValues:
            if newCard == c and oldCard == c:
                break
            elif oldCard == c:
                return True
            elif newCard == c:
                return False

def sortHandsWithinTypes(currentHands : list, hand : dict, isPart2 : bool = 0):
    # return the revised list by inserting the new hand at the correct location

    for handNumber in range(len(currentHands)):
        if newHandLessThanOldHand(currentHands[handNumber], hand, isPart2):
            currentHands.insert(handNumber, hand)
            break
    else: # i.e. if we exit the for loop without breaking
        currentHands.append(hand)

    return currentHands

def solveSorted(finishedSort : list):
    i = 1
    finalSum = 0
    for handtype in finishedSort:
        for hand in handtype:
            finalSum += (i * hand["bid"])
            i += 1
    
    return finalSum

formatted_input = parseInput("7/input.txt")
sorted_input = sortHands(formatted_input)
output = solveSorted(sorted_input)
print("part 1 solution is {}".format(output))

sorted_input_part2 = sortHands(formatted_input, True)
output_part2 = solveSorted(sorted_input_part2)
print("part 2 solution is {}".format(output_part2))