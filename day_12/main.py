

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
def solve(line, errors, branch="", fullLine=""):
    out = 0
    global solDic 

    if(type(line) == str):
        line = list(line)

    
    print(branch, "line", "".join(line), "errors", errors)
    #print(branch, "fl", fullLine)
    k = str([line, errors])
    if(k in solDic):
        return solDic[k]
    

    if(len(errors) == 0):
        print("here")
        return 1
    else:
        if(len(line) == 0):
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
                out+= solve(line[1:], errors.copy(), branch+bb, fullLine+"#")
        else:
            #TODO next char should only be . or ? 
            if(nxt != "#"): 
                line2 = line.copy()
                try:
                    line2[1] = "."
                except:
                    pass
                
                out += solve(line2[1:], errors[1:], branch+bb, fullLine + ".")
            else:
                return 0
   


    if(line[0] == "?"):
        # 2 ways it either can be a # or a .
        l1 = line.copy()
        l1[0] = "#"
        l2 = line.copy()
        l2[0] = "."
        

        out+=solve(l1, errors.copy(), branch+bb, fullLine + "#")
        out+=solve(l2, errors.copy(), branch+bb, fullLine + ".")

    return out


















    if(line[0] == "#"):
        if(errors[0] > 0):
            errors[0] -= 1

        if(errors[0] == 0):
            out += solve(line[2:], errors[1:], branch+"    ")
        else:
            pass
            #TODO check wether next char is a # and then spawn new solve

    if(line[0] == "."):
        out+= solve(line[1:], errors)

    if(line[0] == "?"):    
        print(branch, "selecting dot")
        newLine1 = line.copy()
        newLine1[0] = "."
        out += solve(newLine1[1:], errors, branch+"    ")
        

        print(branch, "selecting #")
        newLine2 = line.copy()
        newLine2[0] = "#"
        err2 = errors.copy()
        err2[0] -= 1

        out+= solve(newLine2, err2, branch+"    ")
        nextIsDot = 0




    return out

















    inBlock = 0
    nextIsDot = 0
    
    for ll in range(len(line)):
        if(line[ll] == "?"):
            newLine1 = line.copy()
            newLine1[ll] = "."
            out += solve(newLine1[ll:], errors, branch+"    ")
           
           
            if(nextIsDot == 0):
                newLine2 = line.copy()
                newLine2[ll] = "#"
                err2 = errors.copy()
                err2[0] -= 1

                out+= solve(newLine2, err2, branch+"    ")
                nextIsDot = 0


        if(line[ll] == "."):
            if(inBlock):
                if(errors[0] != 0):
                    print(branch, "can't be done, returning 0")
                    return 0
                else:
                    out += solve(line[ll+1:], errors[1:], branch+"    ")
            nextIsDot = 0

        if(line[ll] == "#"):
            if(nextIsDot == 1):
                print(branch, "can't be done, returning 0")
                return 0 
            inBlock = 1
            errors[0] -= 1
            if(errors[0] <= 0):
                nextIsDot = 1

    return 1

for l in lines:
    record = l.split(" ")[0]
    nums = l.split(" ")[1].split(",")
    nums = [int(i) for i in nums] 
    print("solutions? :",solve(l.split(" ")[0], nums))




