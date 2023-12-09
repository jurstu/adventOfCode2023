

with open("in") as f:
    d = f.read()



d = d.split("\n")[:-1]
d = [[int(x) for x in d[k].split(" ")] for k in range(len(d))] 






def calcDiff(l):
    out = []
    for i in range(len(l)-1):
        out.append(l[i+1] - l[i])
    return out


def isZeros(l):
    return set(l) == set([0])

def calcTriangle(dd):   
    out = [dd]
    while(isZeros(dd) == False):
        newOut = calcDiff(dd)
        out.append(newOut)
        dd = newOut
    return out


def solveTriangle(dd, secondPart=0):
    
    if(secondPart == 0):
        for l in range(len(dd)-1, 0, -1):
            #print(l, dd[l])
            dd[l-1].append(dd[l-1][-1] + dd[l][-1])
        return dd[0][-1]
    else:
        carry = 0
        for l in range(len(dd)-1, -1, -1):
            print("dd[l][0]", dd[l][0])
            carry = -carry + dd[l][0]

        print(carry)
        return carry


add = 0
for hist in d:
    t = calcTriangle(hist) 
    add += solveTriangle(t)
    

print("############# part one", add)


add = 0
for hist in d:

    t = calcTriangle(hist)
    print(t)
    add += solveTriangle(t, 1)

print("part two", add)

