s = open('input.txt','r').read()


s = [k for k in s.split("\n")]
active = set()

for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == '#':
            active.add((i, j, 0))
for cycles in range(6):
    a2 = []
    for xx in range(-20, 20):
        for yy in range(-20, 20):
            for zz in range(-20, 20):
                neigh = 0
                p = [xx,yy,zz]
                for x in range(xx-1,xx+2):
                    for y in range(yy-1,yy+2):
                        for z in range(zz-1,zz+2):
                            if [x,y,z] == p:continue
                            if (x,y,z) in active:
                                neigh += 1
                if (xx,yy,zz) in active and 2 <= neigh <= 3:
                    a2 += [(xx,yy,zz)]
                elif (xx,yy,zz) not in active and neigh == 3:
                    a2 += [(xx,yy,zz)]
    active = set(a2)
print(len(active),flush=True)
