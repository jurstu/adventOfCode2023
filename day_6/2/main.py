import math

f = open("in", "r")
d = f.read()
f.close()

















row1 = d.split("\n")[0].split(":")[1].split(" ")
row2 = d.split("\n")[1].split(":")[1].split(" ")

times = []
dists = []
for e in row1:
    try:
        times.append(int(e))
    except:
        pass

for e in row2:
    try:
        dists.append(int(e))
    except:
        pass

waysAll = []
ways = 0
for race in range(len(times)):
    t = times[race]
    d = dists[race]

    # d = (t-v)*v,   where v is selected speed, and t is whole available time
    # d > d_record
    # tv - v^2 - d_r > 0
    # 
    # -v^2 + tv - d_r > 0
    #
    # a = -1
    # b = t
    # c = -d_r
    # 
    # so
    # delta = t^2 - 4d_r

    delta = t*t - 4*d
    if(delta > 0):
        v2 = -(-t - math.sqrt(delta))/2
        v1 = -(-t + math.sqrt(delta))/2 
        print(v1, v2)
        
        if(v1 - int(v1) == 0):
            fr = v1+1
        else:
            fr = math.ceil(v1)


        if(v2 - int(v2) == 0):
            to = v2-1
        else:
            to = math.floor(v2)





        print(fr, to, to-fr+1)

        ways = to-fr+1
        waysAll.append(ways)
        print("#################")


    else:
        ways = 0
    






print(times)
print(dists)

out = waysAll[0]
for i in range(1,len(waysAll)):
    out*=waysAll[i]


print(int(out))

