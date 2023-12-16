
d = ""
with open("in") as f:
    d = f.read()

tokens = d.strip().split(",")

s = 0
for token in tokens:
    val = 0
    for c in token:
        print(c)
        val+=ord(c)
        val*=17
        val%=256
    
    s += val
    print(val)

print(s)

