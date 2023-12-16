

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

for blocks in quizes:
    

    lines = blocks.split("\n")
    
    
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
                    print("vertical", k)
                    vsum += k
                else:
                    print("horizontal", k)
                    hsum += k
        
        lines = transform(lines)
    
    
    




print(hsum*100 + vsum)





        
