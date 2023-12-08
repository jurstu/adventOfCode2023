import time

d = ""
with open("in") as f:
    d = f.read()

dirs = d.split("\n")[0]
rest = d.split("\n")[2:-1]

print (dirs, rest)

nodes = {}
for node in rest:
    root = node.split(" = ")[0]
    L = node.split(" = ")[1].split(",")[0][1:]
    R = node.split(" = ")[1].split(",")[1][1:-1]
    print(root, L, R)

    nodes[root] = [L, R]

print(nodes)

cnt = 0

dirInd = 0
currNode = "AAA"
while(currNode != "ZZZ"):
    if dirs[dirInd] == "L":
        ind = 0
    else:
        ind = 1
    print(ind)
    
    currNode = nodes[currNode][ind]
    dirInd = (dirInd+1)%len(dirs)
    cnt+=1    
    #time.sleep(10)



print(cnt)
