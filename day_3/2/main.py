


f = open("in", "r")
d = f.read()
f.close()

#print(d)


stars = []
numbers = {}




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
        if a[i] == '*':
            return  1
    return 0


lines = d.split("\n")[:-1]
#lines is our 2d matrix
out = 0
number = 0
addFlag = 0



for y in range(len(lines)):
    line = lines[y]
    for x  in range(len(line)):
        c = line[x]
        if(c == "*"):
            stars.append([x, y])

print(stars)


numLen = 0
addNum = 0
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
            numLen+=1
            addNum = 1
        else:
            if(addNum):
                for l in range(numLen):
                    key = [x-l-1, y]
                    #print(key)
                    numbers [str(key)] = number
                numLen=0
                addNum = 0
            number = 0
    
    if(addNum):
        print("number from end of line", number)
        x = len(line) - 1
        for l in range(numLen):
            key = [x-l-1, y]
            numbers[str(key)] = number

    addNum = 0


print(numbers)
#print(stars)


for star in stars:
    a = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    a[0] = [star[0]  , star[1]+1]
    a[1] = [star[0]  , star[1]-1]
    a[2] = [star[0]+1, star[1]+1]
    a[3] = [star[0]-1, star[1]+1]
    a[4] = [star[0]+1, star[1]-1]
    a[5] = [star[0]-1, star[1]-1]
    a[6] = [star[0]+1, star[1]  ]
    a[7] = [star[0]-1, star[1]  ]
    


    mul = set()
    for aa in a:
        if(str(aa) in numbers):
            print("star", star, "has a number", numbers[str(aa)])
            mul.add(numbers[str(aa)])
       
    mul = list(mul)
    print(mul)
    if(len(mul) == 2):
        out += mul[0] * mul[1]
#    else:
#        out += mul[0]**2




print(out)
