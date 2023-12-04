import json




f = open("in", "r")
d = f.read()
f.close()



cardsOrig = d.split("\n")[:-1]


winningNumbers = []

cardsDict = []




for i, card in enumerate(cardsOrig):
    our = card.split("|")[-1]
    winning = card.split(":")[1].split("|")[0]
    








    our = [int(our[i*3:i*3+3]) for i in range(len(our)//3)] 
    winning = [int(winning[i*3:i*3+3]) for i in range(len(winning)//3)] 

    cardsDict.append([winning, our, i+1])


out = len(cardsDict)

originalCards = cardsDict.copy()



newSet = {}
while (len(cardsDict) > 0):
    # TODO do all the stuff required to make new set
    newSet = [] 

    for i in range(len(cardsDict)):
        card = cardsDict[i]

        add = 0
        for our in card[1]:
            if our in card[0]:
                add+=1

        try:
            for kk in range(add):
                newSet.append(originalCards[card[2] + kk])
        except:
            pass
        
        print("card ", card, "has ", add, "good numbers, len of newSet", len(newSet))
    #print(json.dumps(newSet, indent=4))


    out += len(newSet)
    # TODO rewrite newSet to cardsDict
    cardsDict = []
    for n in newSet:
        cardsDict.append(n)



print(out)
#print(json.dumps(newSet, indent=4))

