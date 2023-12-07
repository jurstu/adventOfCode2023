

d = ""
with open("in") as f:
    d = f.read()

hands = [card.split(" ")[0] for card in d.split("\n")[:-1]]
bids =  [card.split(" ")[1] for card in d.split("\n")[:-1]]


print(hands)

cards = {
            "A": 0,
            "K": 1,
            "Q": 2,
            "J": 3,
            "T": 4,
            "9": 5,
            "8": 6, 
            "7": 7,
            "6": 8,
            "5": 9,
            "4": 10,
            "3": 11,
            "2": 12
        }

def isHandABiggerThanB(handA):
    handA = handA[0]
    out = 0
    for a in handA:
       out = out*15 + cards[a]
    return out


def isFiveOfAKind(hand):
    return hand[0] == hand[1] == hand[2] == hand[3] == hand[4]


def isFourOfAKind(hand):
    d = {}
    for card in hand:
        if not card in d:
            d[card] = 1
        else:
            d[card] += 1

    for k in d:
        if(d[k] >= 4):
            return True
    return False

def isFullHouse(hand):
    d = {}
    for card in hand:
        if not card in d:
            d[card] = 1
        else:
            d[card] += 1
    
    b = set(d.values())
    if b == set([2, 3]):
        return True
    return False


def isThreeOfAKind(hand):
    d = {}
    for card in hand:
        if not card in d:
            d[card] = 1
        else:
            d[card] += 1
    
    b = set(d.values())
    if b == set([3, 1, 1]):
        return True
    return False

def isTwoPair(hand):
    d = {}
    for card in hand:
        if not card in d:
            d[card] = 1
        else:
            d[card] += 1
    
    n = 0
    for k in d.values():
        if k == 2:
            n+=1

    if(n == 2):
        return True
    return False


def isOnePair(hand):
    d = {}
    for card in hand:
        if not card in d:
            d[card] = 1
        else:
            d[card] += 1
    
    n = 0
    for k in d.values():
        if k == 2:
            n+=1

    if(n == 1):
        return True
    return False

 
def isHighCard(hand):
    d = {}
    for card in hand:
        if not card in d:
            d[card] = 1
        else:
            d[card] += 1
    
    n = 0
    for k in d.values():
        if k == 1:
            n+=1

    if(n == 5):
        return True
    return False




#print(isHandABiggerThanB(hands[1], hands[0]))
#print(isFiveOfAKind("aaaaa"))
#print(isFourOfAKind("aaaaa"))
#print(isFullHouse("aabbb"))
#print(isThreeOfAKind("1abbb"))
#print(isTwoPair("11bbb"))
#print(isTwoPair("11abb"))
#print(isOnePair("11dfb"))
#print(isHighCard("12a35"))



# winTypes = 0, 1, 2, 3, 4, 5, 6
# 
# 0 5oak
# 1 4oak
# ...


handsRanks = []



for hand in hands:
    if(isFiveOfAKind(hand)):
        handsRanks.append(0)
    elif(isFourOfAKind(hand)):
        handsRanks.append(1)
    elif(isFullHouse(hand)):
        handsRanks.append(2)
    elif(isThreeOfAKind(hand)):
        handsRanks.append(3)
    elif(isTwoPair(hand)):
        handsRanks.append(4)
    elif(isOnePair(hand)):
        handsRanks.append(5)
    elif(isHighCard(hand)):
        handsRanks.append(6)
    else:
        handsRanks.append(7)


print(handsRanks)

out = 0

t = []
last = 0
for i in range(8):
    t = []
    for k in range(len(handsRanks)):
        if(handsRanks[k] == i):
            t.append([hands[k], bids[k], i])

    t = sorted(t, key=isHandABiggerThanB)

    print(t)
    zz = len(handsRanks)
    for k in range(len(t)):
        rank = zz - k - last
        print(rank)
        out += int(t[k][1]) * (rank)
    last += len(t)

print(out)




