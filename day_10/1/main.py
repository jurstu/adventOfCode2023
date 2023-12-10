



with open("in") as f:
    d = f.read()

rows = d.strip().split("\n")

print(d)
lenMap = [[-1 for i in range(len(r))] for r in rows]

print(lenMap)

def findStart(m):
    print(m)
    for y, r in enumerate(m):
        if "S" in r:
            x = r.index("S")
            return (x, y)


# NS EW 
# UD RL
# 
dirMap = {
        "|": 0b1100,
        "-": 0b0011,
        "F": 0b0110,
        "J": 0b1001,
        "L": 0b1010,
        "7": 0b0101,
        ".": 0b0000,
        "S": 0b1111
}



def getNextPoint(p, m):
    out = 0b0000
    c = m[p[1]][p[0]]
    print(c) 
    u = "."  
    d = "." 
    l = "." 
    r = "." 
    try:
        u = m[p[1] - 1][p[0]]
    except:
        pass
    
    try:
        d = m[p[1] + 1][p[0]]
    except:
        pass

    try:
        l = m[p[1]][p[0] - 1]
    except:
        pass

    try:
        r = m[p[1]][p[0] + 1]
    except:
        pass

    u = dirMap[u]
    d = dirMap[d]
    l = dirMap[l]
    r = dirMap[r]

    out = []
    if(c in dirMap):
        c = dirMap[c]
          
        if(c & 0b1000 and (u & 0b0100)): 
            out.append([p[0], p[1]-1])
    
        if(c & 0b0100 and (d & 0b1000)): 
            out.append([p[0], p[1]+1])

        if(c & 0b0010 and (r & 0b0001)): 
            out.append([p[0]+1, p[1]])

        if(c & 0b0001 and (l & 0b0010)): 
            out.append([p[0]-1, p[1]])

    return out
    



ways=[findStart(rows)]
print("ways is", ways)
allEnd = 0
allreadyVisited = {str(ways[0]):1}
cnt = 0
while(len(ways) != 0):
    nextWays = []
    for w in ways:
        lenMap[w[1]][w[0]] = cnt
        dirs = getNextPoint(w, rows)  
        for d in dirs:
            if(str(d) in allreadyVisited):
                pass
            else:
                nextWays.append(d)
                allreadyVisited[str(d)] = 1
             
    cnt+=1
    ways = nextWays 




print(lenMap)
print(dirs)



print("max is", max(map(max, lenMap)))
