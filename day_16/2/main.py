

with open("in") as f:
    d = f.read().strip().split("\n")



dirs = {
        "n": [0, 1],
        "s": [0, -1],
        "e": [1, 0],
        "w": [-1, 0]
        }



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





def solveForStart(start):
    visited = {} 
    paths = [start]
    while(len(paths) != 0):
        newPaths = []
        #print(paths) 
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

    return len(visited.keys())

outs = []

for x in range(len(d[0])):
    p = [x, -1, "n"]
    outs.append(solveForStart(p))
    p = [x, len(d), "s"]
    outs.append(solveForStart(p))


for y in range(len(d)):
    p = [-1, y, "e"]
    outs.append(solveForStart(p))
    p = [len(d[0]), y, "w"]
    outs.append(solveForStart(p))







print(outs)
print(max(outs))


















