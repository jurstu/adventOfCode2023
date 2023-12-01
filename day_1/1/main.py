


f = open("in2", "r")
d = f.read()
f.close()


lines = d.split("\n")[:-1]
out = []

s = 0

print(lines)
for line in lines:
    first = -1
    last = 0
    print(line)
    for c in line:
        if '0' <= c <= '9':
            last = c
            if(first == -1):
                first = c
    s+= int(first+last)

print(s)
