
def checkSeq(line, seq):
    re = True
    for i in range(len(seq)):
        pass


def changeWordsToLetters(line):
    digitsStr = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
        ]

    





    return line


digitsStr = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
        ]


f = open("in", "r")
d = f.read()
f.close()

lines = d.split("\n")[:-1]

ss=0
linesFilt = []
for line in lines:
    lastStart=0
    lineOut = ""
    print("full line", line)
    for i in range(len(line)):

        block = line[lastStart:i+1]

        print("block is", block)
        for d in range(len(digitsStr)):
            exch = d+1
            s = digitsStr[d]
            if(s in block):
                print("fffound", s)
                lineOut += str(exch) 
                lastStart = i
                continue
        
        if(('0' <= line[i] <= '9')):
            lineOut += line[i]
            lastStart = i + 1
            print("found a number", line[i])
    print(lineOut)    
    linesFilt.append(lineOut)



ss = 0
for line in linesFilt:
    first = -1
    last = 0
    for c in line:
        if '0' <= c <= '9':
            last = c
            if(first == -1):
                first = c
    ss += int(first+last)



print("all", ss)


#54689
