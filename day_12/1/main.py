

d = ""
with open("in") as f:
    d = f.read()

lines = d.strip().split("\n")

solDic = {}


#     #?      1  -> 1 
#     ?#      1  -> 1
#     ??      1  -> 1
#     

bb = " |  "
def solve(line, errors, branch="", fullLine="", nextC = 0):
    out = 0
    global solDic 

    if(type(line) == str):
        line = list(line)

    
#    print(branch, "line", "".join(line), "errors", errors, "nextC", nextC)
    #print(branch, "fl", fullLine)
    k = str([line, errors])
    if(k in solDic):
        return solDic[k]
    

    
    if(len(errors) == 0):
        print("here")
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
        out += solve(line[1:], errors.copy(), branch+bb, fullLine + ".")

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
                out+= solve(line[1:], errors.copy(), branch+bb, fullLine+"#", 1)
        else:
            out += solve(line[1:], errors[1:], branch+bb, fullLine + ".", -1)


    if(line[0] == "?"):
        # 2 ways it either can be a # or a .

        if(nextC != -1):
            l1 = line.copy()
            l1[0] = "#"
            out+=solve(l1, errors.copy(), branch+bb, fullLine + "#")
        
        if(nextC != 1):
            l2 = line.copy()
            l2[0] = "."
            out+=solve(l2, errors.copy(), branch+bb, fullLine + ".")

    return out





s = 0
for l in lines:
    record = l.split(" ")[0]
    nums = l.split(" ")[1].split(",")
    nums = [int(i) for i in nums] 
    s+= solve(l.split(" ")[0], nums)

print(s)




