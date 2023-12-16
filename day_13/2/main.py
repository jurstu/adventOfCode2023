

def transform(lines):
    up = [""] * len(lines[0])    
    for y in range(0, len(lines)): 
        l = lines[y]
        for x in range(len(l)):
            up[x] += lines[y][x]
    
    
    return up.copy()

with open("in") as f:
    d = f.read()


quizes = d.strip().split("\n\n")
hsum = 0
vsum = 0




def solveBlock(lines, vOrig=-1, hOrig=-1):
    hsum = 0
    vsum = 0
    for v in range(2):
        lDict = {}
        for iii, l in enumerate(lines):
            #print("line is", l)
            dl = {}
            dr = {}
            for ll in range(1, len(l)): #checking all mirrors in this line
                left = l[0:ll][::-1]
                reft = l[ll:]
                allGood = 1
                for i in range(min(len(left), len(reft))):
                    if(left[i] != reft[i]):
                        allGood = 0
                        break
        
                # allGood means if this offset has a mirror
        
                if(allGood and iii == 0):
                    #print("here", ll, left, reft)
                    lDict[ll] = 1
                elif(allGood and iii != 0):
                    if(ll in lDict):
                        lDict[ll] += 1
                    #else:
                    #    print("this mirror ain't in first line")
        
        
        for k in lDict:
            if(lDict[k] == len(lines)):
                if(v == 0):
                    if(vOrig != k):
                        print("vertical", k)
                        vsum = k
                else:
                    if(hOrig != k):
                        print("horizontal", k)
                        hsum = k
        
        lines = transform(lines)
    return vsum, hsum



outH = 0
outV = 0

def flip(c):
    if c=="#":
        return "."
    else:
        return "#"


for blocks in quizes:
    lines = [list(x) for x in list(blocks.split("\n"))]


    outFlag = 0
    print("#######################")
#    print(lines)
    v, h = solveBlock(lines)
    print("orig", v, h)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            lines[y][x] = flip(lines[y][x])
            v2, h2 = solveBlock(lines, v, h)

            if(v2 != v and v2 != 0):
                outV += v2
                outFlag = 1
                print("found V", v2)


            if(h2 != h and h2 != 0):
                outH += h2
                outFlag = 1
                print("found H", h2)

            if(outFlag):
                break
            lines[y][x] = flip(lines[y][x])
        if(outFlag):
            break
    
    
    



print(outH*100 + outV)





        
