def parseInput(path : str):
    with open(path) as rawtxt:
        hands = []

        for line in rawtxt:
            a, b = line.split()
            formattedline = {"cards" : a, "bid" : int(b)}
            hands.append(formattedline)

        return hands
    
def sortHands(hands : list[dict["cards" : str, "bid" : int]]):

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
        # start by sorting the hand into its type by using the number of character repeats
        quickCount = len(set(c for c in hand["cards"]))

        if quickCount == 5: # 5 different cards
            handTypes[highCard] = sortHandsWithinTypes(handTypes[highCard], hand)
            
        elif quickCount == 4: # 4 different
            #handTypes[pair].append(hand)
            handTypes[pair] = sortHandsWithinTypes(handTypes[pair], hand)

        elif quickCount == 1: # ding ding ding
            #handTypes[fiveOfAKind].append(hand)
            handTypes[fiveOfAKind] = sortHandsWithinTypes(handTypes[fiveOfAKind], hand)

        elif quickCount == 2: # four of a kind OR full house
            if hand["cards"].count(hand["cards"][0]) in (1,4):
                #handTypes[fourOfAKind].append(hand)
                handTypes[fourOfAKind] = sortHandsWithinTypes(handTypes[fourOfAKind], hand)
            else: #handTypes[fullHouse].append(hand)
                handTypes[fullHouse] = sortHandsWithinTypes(handTypes[fullHouse], hand)

        else: # three of a kind OR two pair
            assert quickCount == 3
            for c in hand["cards"]: # first card 
                cardCount = hand["cards"].count(c)
                if cardCount == 2:
                    #handTypes[twoPair].append(hand)
                    handTypes[twoPair] = sortHandsWithinTypes(handTypes[twoPair], hand)
                    break
                elif cardCount == 3:
                    #handTypes[threeOfAKind].append(hand)
                    handTypes[threeOfAKind] = sortHandsWithinTypes(handTypes[threeOfAKind], hand)
                    break

    return handTypes


def newHandLessThanOldHand(oldHand, newHand):
    cardValues = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for i in range(5): # 5 cards per hand
        oldCard = oldHand["cards"][i] # ith letter of old hand
        newCard = newHand["cards"][i]
        for c in cardValues:
            if newCard == c and oldCard == c:
                break
            elif oldCard == c:
                return True
            elif newCard == c:
                return False

def sortHandsWithinTypes(currentHands : list, hand : dict):
    # return the revised list by inserting the new hand at the correct location

    for handNumber in range(len(currentHands)):
        if newHandLessThanOldHand(currentHands[handNumber], hand):
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
print("part 2 solution is {}".format(output))