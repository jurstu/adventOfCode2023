
with open("in") as f:
    d = f.read()

d = d.strip().split()
d = [list(x) for x in d]

dd = d.copy()


print(d)
for y, l in enumerate(d):
    for x, c in enumerate(l):
        if(c == "O"):
            print("found O")
            for yy in range(y - 1, -1, -1):
                if(d[yy][x] == "."):
                    d[yy+1][x] = "."
                    d[yy][x] = "O"
                    print("moved")
                else:
                    break


print(d)


out = 0
for y, l in enumerate(d):
    for x, c in enumerate(l):
        if(c == "O"):
            out += (len(d) - y)
print(out)
