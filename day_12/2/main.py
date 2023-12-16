

d = ""
with open("in") as f:
    d = f.read()

lines = d.strip().split("\n")



def red(line):
    out = ""
    flag = 0
    for i in range(len(line)):
        if(line[i] == "." and flag):
            pass
        elif(line[i] == "."):
            out += "."
            flag = 1
        else:
            out+=line[i]
            flag = 0

    return out


solDic = {}

bb = " |  "
def solve(line, errors, branch=1, fullLine="", nextC = 0):
    out = 0
    global solDict


    if(type(line) == str):
        line = list(line)

    #print("depth=", branch)
    
#    print(branch, "line", "".join(line), "errors", errors, "nextC", nextC)
    #print(branch, "fl", fullLine)
    k = str([line, errors])
    if(k in solDic):
        return solDic[k]
    

    
    if(len(errors) == 0):
        #print("here")
        for x in line:
            if(x == "#"):
                return 0
        return 1
    else:
        if(len(line) == 0):
            return 0 


    if(nextC == 1 and line[0] == "."):
        return 0

    if(nextC == -1 and line[0] == "#"):
        return 0


    if(line[0] == "."):
        out += solve(line[1:], errors.copy(), branch+1, fullLine + ".")

    if(line[0] == "#"):
        errors[0] -= 1

        nxt = ""
        try:
            nxt = line[1]
        except:
            pass

        if(errors[0] > 0):
            #TODO ensure next char isn't .

            if(nxt == "."):
                return 0  # wee need some more # and we are getting .
            else:
                out+= solve(line[1:], errors.copy(), branch+1, fullLine+"#", 1)
        else:
            out += solve(line[1:], errors[1:], branch+1, fullLine + ".", -1)


    if(line[0] == "?"):
        # 2 ways it either can be a # or a .

        if(nextC != -1):
            l1 = line.copy()
            l1[0] = "#"
            out+=solve(l1, errors.copy(), branch+1, fullLine + "#")
        
        if(nextC != 1):
            l2 = line.copy()
            l2[0] = "."
            out+=solve(l2, errors.copy(), branch+1, fullLine + ".")

    return out





s = 0
for iii, l in enumerate(lines):

    print(iii, "from", len(lines))
    record = l.split(" ")[0]
    nums = l.split(" ")[1].split(",")
    nums = [int(i) for i in nums] 


    nums = 5*nums

    ll = l.split(" ")[0]
    llm =  ll + "?" + ll + "?" + ll + "?" + ll + "?" + ll
    ll = llm

    #print(ll, nums)
    
    ll = red(ll)
    #print(ll)
    #if(iii == 2):
    #    break
    s+= solve(ll, nums)

print(s)




