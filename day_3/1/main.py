


f = open("in", "r")
d = f.read()
f.close()

#print(d)

def isDigit(c):
    if ord('0') <= ord(c) <= ord('9'):
        return True
    else:
        return False


def charToDigit(c):
    return ord(c) - ord('0')


def getCharFromMap(bitmap, pos):
    h = len(bitmap)
    w = len(bitmap[0])
    if(not(0 <= pos[0] < w)):
        return '.'

    if(not(0 <= pos[1] < h)):
        return '.'

    return bitmap[pos[1]][pos[0]]


def checkAroundForSymbol(bitmap, pos):
    a = ['.', '.', '.', '.', '.', '.', '.', '.', '.']

    a[0] = getCharFromMap(bitmap, [pos[0]+1, pos[1]])
    a[1] = getCharFromMap(bitmap, [pos[0]-1, pos[1]])
    #print(a[1])
    a[2] = getCharFromMap(bitmap, [pos[0]+1, pos[1]+1])
    a[3] = getCharFromMap(bitmap, [pos[0]-1, pos[1]+1])
    a[4] = getCharFromMap(bitmap, [pos[0]+1, pos[1]-1])
    a[5] = getCharFromMap(bitmap, [pos[0]-1, pos[1]-1])
    a[6] = getCharFromMap(bitmap, [pos[0]  , pos[1]+1])
    a[7] = getCharFromMap(bitmap, [pos[0]  , pos[1]-1])
    
    a[8] = getCharFromMap(bitmap, [pos[0]  , pos[1]])
    symbolFound = 0
    for i in range(8):
        if a[i] != '.' and (not isDigit(a[i])):
            return  1
    return 0


lines = d.split("\n")[:-1]
#lines is our 2d matrix
out = 0
number = 0
addFlag = 0

for y in range(len(lines)):
    line = lines[y]
    number = 0
    print(line)
    for x  in range(len(line)):
        c = line[x]
        #print(c)
        #print("addFlag", addFlag)
        if(isDigit(c)):
            number = number*10 +  charToDigit(c)
            #print("number is", number)
            if(checkAroundForSymbol(lines, [x, y])):
                addFlag = 1
        else:
            if(addFlag):
                out += number
                print("adding", number)
            number = 0
            addFlag = 0

    if(addFlag):
        print("adding", number)
        out+=number
        addFlag = 0
        number = 0


print(out)
