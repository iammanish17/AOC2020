s = open('input.txt','r').read()
#s = ''''''

s = [k for k in s.split("\n")]
di = {}

for line in s:
    xx= line
    x, y = 0, 0
    while xx:
        if xx.startswith("sw"):
            xx = xx[2:]
            y -= 1
            x += 1
        elif xx.startswith("se"):
            xx = xx[2:]
            x += 1
        elif xx.startswith("ne"):
            xx = xx[2:]
            x -= 1
            y += 1
        elif xx.startswith("nw"):
            xx = xx[2:]
            x -= 1
        elif xx.startswith("e"):
            xx = xx[1:]
            y += 1
        elif xx.startswith("w"):
            xx = xx[1:]
            y -= 1
    if (x,y) not in di:
        di[(x, y)] = 1
    di[(x, y)] = 1 - di[(x, y)]
k=0
for i in di:
    if di[i] == 0:
        k += 1
print(k)
