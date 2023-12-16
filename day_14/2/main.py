
with open("in") as f:
    d = f.read()

d = d.strip().split()
d = [list(x) for x in d]

dd = d.copy()



def transform(lines):
    up = [""] * len(lines[0])
    for y in range(0, len(lines)):
        l = lines[y]
        for x in range(len(l)):
            up[x] += lines[y][x]


    return up.copy()



def transformBack(cols):
    right = [""] * len(cols[0])
    for x in range(0, len(cols)):
        col = cols[x]
        for y in range(len(col)):
            right[y] += cols[x][y]


    return right.copy()





def pushN(d):
    # north
    if(type(d[0]) == str):
        d = [list(x) for x in d]
    for y, l in enumerate(d):
        for x, c in enumerate(l):
            if(c == "O"):
                
               for yy in range(y - 1, -1, -1):
                   if(d[yy][x] == "."):
                       d[yy+1][x] = "."
                       d[yy][x] = "O"
                       #print("moved")
                   else:
                       break
    return d



def pushW(d):
    # west
    #print("before rotation")
    #showMap(d)
    work = transform(d)
    work = [list(x) for x in work]
    #print("after rotation")
    #print("west rotated map")
    #showMap(work)

    work = pushN(work)

    d = transformBack(work)
    #print("after \"westing\"")
    #showMap(work)


    return d


def pushS(d):
    # south
    d = [list(x) for x in d]
    for y, l in reversed(list(enumerate(d))):
        for x, c in enumerate(l):
            if(c == "O"):
                for yy in range(y+1, len(d)):
                    if(d[yy][x] == "."):
                        d[yy-1][x] = "."
                        d[yy][x] = "O"
                #        print("moved")
                    else:
                        break
    
    #print("d after south", "\n" + "\n".join(["".join(x) for x in d]))
    return d


def pushE(d):
    #east
    #showMap(d)
    work = transform(d)
    work = [list(x) for x in work[::-1]]
    #print("\n\n" + "\n".join(["".join(x) for x in work]))
   
    work = pushN(work)

    d = transformBack(work[::-1])
    return d



#print("\n\nd after east", "\n" + "\n".join(d))

def showMap(d):
    pass
    print("\n\n" + "\n".join(["".join(x) for x in d]))

'''
from copy import deepcopy

showMap(pushN(deepcopy(d)))
showMap(pushW(deepcopy(d)))
showMap(pushS(deepcopy(d)))
showMap(pushE(deepcopy(d)))
'''

#for i in range(

from copy import deepcopy

a = list([list(x) for x in d])
print(a)

for i in range(1000):
    if(i % 1000 == 0):
        print(i)
    


    try:
        lastA = deepcopy(a)
    except:
        pass


    
    a = deepcopy(pushN(a))
    a = deepcopy(pushW(a))
    a = deepcopy(pushS(a))
    a = deepcopy(pushE(a))
    
    showMap(a)









d = deepcopy(a)






'''
n = pushN(d)
w = pushW(n)
s = pushS(w)
e = pushE(s)

showMap(e)
'''











out = 0
for y, l in enumerate(d):
    for x, c in enumerate(l):
        if(c == "O"):
            out += (len(d) - y)
print(out)

