

def getDest(m, val):
    for mm in m:
        if mm[1] <= val < (mm[1] + mm[2]):        
            out = mm[0] + (val - mm[1]) 
            return out 
    return val


d = ""
with open("in") as f:
    d = f.read()


seeds = [int(val) for val in d.split("\n")[:-1][0].split(":")[1].split(" ")[1:]]


k = 0
m = 0

maps = d.strip().split("\n\n")[1:]

maps = [a.split("\n")[1:] for a in maps]

for i in range(len(maps)):

    m = [[int(mm) for mm in maps[i][z].split(" ")] for z in range(len(maps[i]))]
    maps[i] = m


out = []
print(len(seeds))
for i in range(len(seeds)//2):
    print("checking range", seeds[i*2], "to", seeds[i*2] + seeds[i*2+1]-1)
    for kk in range(seeds[i*2], seeds[i*2] + seeds[i*2+1]):
        print(kk)
        dest = kk
        for m in maps:
            dest = getDest(m, dest)
            #print(dest)
    
        #print("###########")
        out.append(dest)


print(out)

print(min(out))



