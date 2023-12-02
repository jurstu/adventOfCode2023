 



f = open("in", "r")
d = f.read()
f.close()

maxR = 12
maxG = 13
maxB = 14

lines = d.split("\n")[:-1]

out = 0

gamesPowers = []

for game in lines:
    minR = 0
    minG = 0
    minB = 0


    gameNumber = int(game.split(" ")[1].split(":")[0])
    #print(gameNumber)
    reaches = game.split(":")[-1].split(";")
    print(reaches)
    for reach in reaches:
        colors = reach.split(", ")
#        print(colors)
        for c in colors:
            ddd = c.split(" ")
            col = ddd[-1]
            amount = int(ddd[-2])

            if(col == "red"):
                minR = max(minR, amount)
            if(col == "green"):
                minG = max(minG, amount)
            if(col == "blue"):
                minB = max(minB, amount)

    print("in game", game, "minimum of rgb is", minR, minG, minB)
    gamesPowers.append(minR*minG*minB)

print(sum(gamesPowers))
