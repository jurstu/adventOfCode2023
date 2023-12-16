

with open("in") as f:
    d = f.read().strip().split("\n")



dirs = {
        "n": [0, 1],
        "s": [0, -1],
        "e": [1, 0],
        "w": [-1, 0]
        }

paths = [[-1, 0, 'e']]


def move(pos, d):
    pos[0] += dirs[d][0]
    pos[1] += dirs[d][1]
    return pos

def getChar(x, y):
    return d[y][x]

def inBounds(x, y, w, h):
    if(y >= h or y < 0 or x < 0 or x>=w):
        return False
    return True



visited = {}
while(len(paths) != 0):
    newPaths = []
    for p in paths:
        di = p[2]
        p[0], p[1] = move(p[:2], di)
        if(inBounds(p[0], p[1], len(d[0]), len(d)) == False):
            continue

        #if already been here from this side
        dk = str([p[0], p[1]])
        if(dk in visited and visited[dk] == p[2]):
            continue


        c = getChar(p[0], p[1])
        print(c)
        if(c == "."):
            #nothing, we move along
            visited[str([p[0], p[1]])] = p[2]
            newPaths.append([p[0], p[1], p[2]])
    
        if(c == "|"):
            visited[str([p[0], p[1]])] = p[2]

            if (p[2] == "e" or p[2] == "w"):
                newPaths.append([p[0], p[1], 'n'])
                newPaths.append([p[0], p[1], 's'])
            else:
                newPaths.append([p[0], p[1], p[2]])

        if(c == "-"):
            visited[str([p[0], p[1]])] = p[2]
            
            if (p[2] == "s" or p[2] == "n"):
                newPaths.append([p[0], p[1], 'e'])
                newPaths.append([p[0], p[1], 'w'])
            else:
                newPaths.append([p[0], p[1], p[2]])

        if(c == "/"):
            visited[str([p[0], p[1]])] = p[2]
            
            if (p[2] == "n"):
                newPaths.append([p[0], p[1], 'w'])
            if (p[2] == "e"):
                newPaths.append([p[0], p[1], 's'])
            if (p[2] == "s"):
                newPaths.append([p[0], p[1], 'e'])
            if (p[2] == "w"):
                newPaths.append([p[0], p[1], 'n'])
        
        if(c == "\\"):
            visited[str([p[0], p[1]])] = p[2]
            
            if (p[2] == "n"):
                newPaths.append([p[0], p[1], 'e'])
            if (p[2] == "e"):
                newPaths.append([p[0], p[1], 'n'])
            if (p[2] == "s"):
                newPaths.append([p[0], p[1], 'w'])
            if (p[2] == "w"):
                newPaths.append([p[0], p[1], 's'])

    paths = newPaths 




print(len(visited.keys()))    



















