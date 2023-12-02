 



f = open("in", "r")
d = f.read()
f.close()

maxR = 12
maxG = 13
maxB = 14

lines = d.split("\n")[:-1]

ggs = set()
out = 0

for game in lines:
    gameNumber = int(game.split(" ")[1].split(":")[0])
    #print(gameNumber)

    reaches = game.split(":")[-1].split(";")

    print(reaches)
    gg = 1

    for reach in reaches:
        colors = reach.split(", ")
#        print(colors)
        for c in colors:
            ddd = c.split(" ")
            col = ddd[-1]
            amount = int(ddd[-2])

            if(col == "red" and (amount > maxR)):
                gg = 0
            if(col == "green" and (amount > maxG)):
                gg = 0
            if(col == "blue" and (amount > maxB)):
                gg = 0
    if gg == 1:
        ggs.add(gameNumber)     
        out += gameNumber
print(ggs)

print(out)
