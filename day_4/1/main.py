




f = open("in", "r")
d = f.read()
f.close()



cards = d.split("\n")[:-1]

out = 0

winningNumbers = []
for card in cards:
    our = card.split("|")[-1]
    winning = card.split(":")[1].split("|")[0]


    our = [int(our[i*3:i*3+3]) for i in range(len(our)//3)] 
    winning = [int(winning[i*3:i*3+3]) for i in range(len(winning)//3)] 

    print(winning)


    cardWin = 0
    for n in our:
        if(n in winning):
            if (cardWin == 0):
                cardWin = 1
            else:
                cardWin *= 2

    out+= cardWin


print(out)


