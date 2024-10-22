def parseInput(path):
    with open(path) as rawtxt:
        hands = []
        for line in rawtxt:
            a, b = line.split()
            formattedline = {"cards" : a, "bid" : int(b)}
            hands.append(formattedline)
        return hands
    
def sortHandsQuickPass(hands):
    roughSort = {
        "Five of a kind" : [],      # AAAAA
        "Four of a kind" : [],      # AA8AA
        "Full house" : [],          # 23332
        "Three of a kind" : [],     # TTT98
        "Two pair" : [],            # 23432
        "One pair" : [],            # A23A4
        "High card" : []            # 23456
        }
    for hand in hands:
        quickCount = len(set(c for c in hand["cards"]))
        if quickCount == 5: # 5 different cards
            roughSort["High card"].append(hand)
        elif quickCount == 4: # 4 different
            roughSort["One pair"].append(hand)
        elif quickCount == 1:
            roughSort["Five of a kind"].append(hand)
        elif quickCount == 2: # four of a kind OR full house
            if hand.count(hand[0]) in (1,4):
                roughSort["Four of a kind"].append(hand)
            else: roughSort["Full house"].append(hand)
        else: # three of a kind OR two pair
            assert quickCount == 3
            for c in hand["cards"]: # first card 
                cardCount = hand["cards"].count(c)
                if cardCount == 2:
                    roughSort["Two pair"].append(hand)
                    break
                elif cardCount == 3:
                    roughSort["Three of a kind"].append(hand)
                    break
    return roughSort

def refineSort(roughSort):
    return