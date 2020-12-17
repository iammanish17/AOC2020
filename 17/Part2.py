s = open('input.txt','r').read()

s = [k for k in s.split("\n")]
active = set()

for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == '#':
            active.add((i, j, 0, 0))
for cycles in range(6):
    a2 = []
    for xx in range(-15, 15):
        for yy in range(-15, 15):
            for zz in range(-15, 15):
                for ww in range(-15, 15):
                    neigh = 0
                    p = [xx,yy,zz,ww]
                    for x in range(xx-1,xx+2):
                        for y in range(yy-1,yy+2):
                            for z in range(zz-1,zz+2):
                                for w in range(ww-1,ww+2):
                                    if [x,y,z,w] == p:continue
                                    if (x,y,z, w) in active:
                                        neigh += 1
                    if (xx,yy,zz,ww) in active and 2 <= neigh <= 3:
                        a2 += [(xx,yy,zz, ww)]
                    elif (xx,yy,zz,ww) not in active and neigh == 3:
                        a2 += [(xx,yy,zz, ww)]
    active = set(a2)
print(len(active),flush=True)
