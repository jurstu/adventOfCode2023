

part = 1

#this doesn't work xd
#part = 1000000

 
d = ""
with open("in") as f:
    d = f.read()

lines = d.strip().split("\n")

galaxies = {}

lines2 = []

for i, r in enumerate(lines):
    if(list(set(r)) == ["."]):
        for p in range(part):
            lines2.append(r)

    lines2.append(r)

lines = lines2
#print(lines)

print("passed rows")

cc = ""
ll = ["" for y in range(len(lines))]

print("passed ll")

for x in range(len(lines[0])):
    cc = ""
    print(x, "in range", len(lines[0]), len(lines))
    for y in range(len(lines)):
        cc += lines[y][x]
    
    print(cc)
    if(set(cc) == set(".")):
        for p in range(part):
            for y in range(len(lines)):
                ll[y] += "."
    for y in range(len(lines)):
       ll[y] += cc[y]
print("gonna look for galaxies")

#for r in ll:
#    print(r)

lines = ll




cnt = 0
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if(c == "#"):
            galaxies[cnt] = [x, y]
            cnt+=1
        
print(galaxies)






lens = []
for x in range(len(galaxies)):
    for zz in range(x+1, len(galaxies)):
        lens.append(abs(galaxies[x][0] - galaxies[zz][0]) + abs(galaxies[x][1] -galaxies[zz][1]))
        print(galaxies[x], galaxies[zz], lens[-1])

print(sum(lens))
