



with open("in") as f:
    d = f.read()

rows = d.strip().split("\n")

#print(d)
lenMap = [[-1 for i in range(len(r))] for r in rows]
nestMap = [["." for i in range(len(r))] for r in rows]

#print(lenMap)

def findStart(m):
    #print(m)
    for y, r in enumerate(m):
        if "S" in r:
            x = r.index("S")
            return [x, y]


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
        "S": 0b1010
}


def printMap(m):
    for r in m:
        out = ""
        for k in r: 
            if (k == "."):
                out+="  ."
            elif(int(k) != -1):
                out+="{: 3d}".format(int(k))
            else:
                out+="   "
        print(out)



def getNextPoint(p, m):
    out = 0b0000
    c = m[p[1]][p[0]]
#    print(c) 
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
            if(c == 0b1100):
                out.append([[p[0], p[1]-1], 'u'])
            else: 
                out.append([[p[0], p[1]-1], ' '])

        if(c & 0b0100 and (d & 0b1000)): 
            if(c == 0b1100):
                out.append([[p[0], p[1]+1], 'd'])
            else: 
                out.append([[p[0], p[1]+1], ' '])
      
        if(c & 0b0010 and (r & 0b0001)): 
            if(c == 0b0011):
                out.append([[p[0]+1, p[1]], 'r'])
            else: 
                out.append([[p[0]+1, p[1]], ' '])
        
        if(c & 0b0001 and (l & 0b0010)): 
            if(c == 0b0011):        
                out.append([[p[0]-1, p[1]], 'l'])
            else: 
                out.append([[p[0]-1, p[1]], ' '])

    return out
    


# 1 movements perpendicular
# 2 check if -1
# 3 add as starting points for multi-point bfs


bd = {      #  x   y
        'u': [ 1,  0],
        'd': [-1,  0],
        'r': [ 0,  1],
        'l': [ 0, -1],
        ' ': [ 0,  0]
        }


ways=[findStart(rows)]
#print("ways is", ways)
allEnd = 0
allreadyVisited = {str(ways[0]):1}
cnt = 0

THE_PATH = []
ENDGAME_SP = []

while(len(ways) != 0):
    nextWays = []
    for w in ways:
        lenMap[w[1]][w[0]] = cnt
        THE_PATH.append(w)
        dirs = getNextPoint(w, rows) 
        for d, dl in dirs:
          


#            if(cccc == "."):
#                
#                print("row", rows[relPos[1]])


            if(str(d) in allreadyVisited):
                continue
            else:

                relMove = bd[dl]
                relPos = [w[0] + relMove[0], w[1] + relMove[1]]
                cccc = " "
                try:
                    cccc = rows[relPos[1]][relPos[0]]
                except:
                    print("err")
                
                if(cccc == "."):
                    #print("row", rows[relPos[1]])
                    print("im at", w)
                    print(cnt, "---", dl, "so checking", relPos, "it's ", cccc)
                    if(relPos not in ENDGAME_SP):
                        ENDGAME_SP.append(relPos)


                nextWays.append(d)
                allreadyVisited[str(d)] = 1
            
            
            #printMap(nestMap)
            #print("current char is", )


            
    cnt+=1
    ways = nextWays 


#for r in rows:
#    print(r)


print("endgame", ENDGAME_SP)






































def canGoThere2(p, rows):
    out = []
    possible = [
                [p[1]-1,p[0]  ],
                [p[1]+1,p[0]  ],
                [p[1],  p[0]+1],
                [p[1],  p[0]-1],
            ]

    for o in possible:
        try:
            if(rows[o[1]][o[0]] == '.'):
                out.append(o)
        except:
            pass

    return out









ways = ENDGAME_SP
visited = {}
for w in ways:
    visited[str(w)] = 1
out = len(ENDGAME_SP)

print("init visit", visited)

while(len(ways) != 0):
    nextWays = []
    for w in ways:
       
        print("im at ", w)
        visited[str(w)] = 1

        dirs = canGoThere2([w[1],w[0]], rows)
        for d in dirs:
            if(str(d) in visited):
                pass
            else:
                visited[str(d)] = 1
                nextWays.append(d)
                out+=1

    print("nextWays", nextWays)
    ways = nextWays

print(out)

exit()
                











exit()

#print(lenMap)
#print(dirs)



#print("max is", max(map(max, lenMap)))
















#for r in lenMap:
#    print(r)














exit()




















#actual part 2 


def getNumbersAround(p, r):
    # urdl
    out = []
    out.append(r[p[1]-1][p[0]  ]) # u 
    out.append(r[p[1]  ][p[0]+1]) # r 
    out.append(r[p[1]+1][p[0]  ]) # d 
    out.append(r[p[1]  ][p[0]-1]) # l
    
    return out

start = findStart(rows)

#print(THE_PATH)

closedPolygons = []
polygonStarted = 0
currPoly = []
startsAndStops = []


for index, point in enumerate(THE_PATH):

    around = getNumbersAround(point, lenMap)
    
    isClose = 1
    for a in around:
        if(a == -1 or index == 0):
            continue
        #print("point ", index, "has a neighboor", a)
        if(abs(a-index) > 1):
            isClose = 0


    if(isClose == 1):
        polygonStarted = 1
    else:
        polygonStarted = 0



    if(polygonStarted):
        currPoly.append([*point, index])
    else:
        if(len(currPoly) > 2):
            closedPolygons.append(currPoly)
            startsAndStops.append([max(currPoly[0][2]-1, 0), min(currPoly[-1][2]+1, len(THE_PATH)-1)])

        currPoly = []



#import json
#print(json.dumps(closedPolygons, indent=4))






#print(startsAndStops)














bestMap = [["." for i in range(len(r))] for r in rows]


# calculate the whole polygon size

def canGoThere(p, rows):
    out = []
    possible = [
                [p[0]-1,p[1]  ],
                [p[0]+1,p[1]  ],
                [p[0],  p[1]+1],
                [p[0],  p[1]-1],
            ]

    for o in possible:
        try:
            if(rows[o[1]][o[0]] == -1):
                out.append(o)
        except:
            pass

    return out




size = len(rows)*len(rows[0])
#print(size)


ways = [[0,0]]

bestMap = lenMap.copy()
alreadyVisited = {str([0,0]): 1}


emptyCnt = 0
while len(ways) > 0:
    nextWays = []
    for w in ways:

        bestMap[w[1]][w[0]] = -4
        emptyCnt += 1
        dirs = canGoThere(w, lenMap)
        for d in dirs:
            if str(d) in alreadyVisited:
                pass
            else:
                alreadyVisited[str(d)] = 1
                nextWays.append(d)
            # check if it's already visited
    ways=nextWays

out = 0
for r in bestMap:
    o = ""
    for e in r:
        if int(e) == -1:
            out+=1
        o+= "{: 3d}".format(int(e))

    print(o)




ways = [findStart(rows)]

#bestMap = lenMap.copy()
alreadyVisited = {str(ways[0]): 1}
print("bestMap", bestMap)

out = 0
while len(ways) > 0:
    nextWays = []
    for w in ways:
        
        if(bestMap[w[1]][w[0]] == -1):
#            print("adding", w, lenMap[w[1]][w[0]])
            out+=1

        dirs = canGoThere2(w, lenMap)
#        print("w", w)
#        print(dirs)
        for d in dirs:
            if str(d) in alreadyVisited:
                pass
                #print("passing")
            else:
                alreadyVisited[str(d)] = 1
                nextWays.append(d)

            # check if it's already visited
    ways=nextWays


print(out)


