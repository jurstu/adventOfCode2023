

part = 1000000

#this doesn't work xd
#part = 1000000

 
d = ""
with open("in") as f:
    d = f.read()

lines = d.strip().split("\n")

galaxies = {}


rowWeights = []
colWeights = []



for i, r in enumerate(lines):
    if(list(set(r)) == ["."]):
        rowWeights.append(part)
    else:
        rowWeights.append(1)



for x in range(len(lines[0])):
    cc = ""
    for y in range(len(lines)):
        cc += lines[y][x]
    
    if(set(cc) == set(".")):
        colWeights.append(part)
    else:
        colWeights.append(1)

cnt = 0
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if(c == "#"):
            galaxies[cnt] = [x, y]
            cnt+=1
        

print("col", colWeights)
print("row", rowWeights)


print(galaxies)

lens = []
for a in range(len(galaxies)):
    for b in range(a+1, len(galaxies)):
        g1 = galaxies[a]
        g2 = galaxies[b]
        ss = 0
        
        print(a, "with", b)

        for x in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
            ss += colWeights[x]
        for y in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
            ss += rowWeights[y]

        lens.append(ss)


print(sum(lens))
