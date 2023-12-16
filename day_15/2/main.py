
d = ""
with open("in") as f:
    d = f.read()

tokens = d.strip().split(",")

def hashIt(token):
    val = 0
    for c in token:
        #print(c)
        val+=ord(c)
        val*=17
        val%=256
    return val




def removeLens(box, label):
    rm = -1
    for i, l in enumerate(box):
        if l[0] == label:
            rm = i
            break
    if(rm != -1):
        del box[rm]
    return box


def replaceAddLens(box, label, focal):
    rm = -1
    for i, l in enumerate(box):
        if(l[0] == label):
            rm = i
            break
    if(rm == -1):
        box.append([label, focal])
    else:
        box[rm] = [label, focal]
    return box


boxes = [[] for i in range(256)]


def printBoxes(b):
    for i, box in enumerate(b):
        if(len(box) != 0):
            out = ""
            for l in box:
                out += "[" + l[0] + " " + str(l[1]) + "], "
            print("box" + str(i) + " " + out)
            

s = 0
for token in tokens:

    if("=" in token):
        label = token.split("=")[0]
        op = "="
        fl = int(token.split("=")[1])

    if("-" in token):
        label = token.split("-")[0]
        op = "-"

    box = hashIt(label)

    if(op == "-"):
        boxes[box] = removeLens(boxes[box], label)


    if(op == "="):
        boxes[box] = replaceAddLens(boxes[box], label, fl)
        


    print("##############", token)
    printBoxes(boxes)
    #print(label, box, op)


out = 0
for i, b in enumerate(boxes):
    for j, l in enumerate(b):
        print(l)
        add = (i+1) * (j+1) * l[1]
        print(add)
        out += add 



print(out)

#print (boxes)




