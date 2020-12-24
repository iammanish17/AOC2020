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
    if di[(x, y)] == 1: di.pop((x, y))

for i in range(100):
    di2 = {}
    for x in range(-102, 102):
        for y in range(-102, 102):
            neighbours = [(x + 1, y - 1), (x + 1, y), (x - 1, y + 1), (x - 1, y), (x, y + 1), (x, y - 1)]
            count = sum(1 if k in di else 0 for k in neighbours)
            if (x, y) in di and 1 <= count <= 2:
                di2[(x, y)] = 0
            if (x, y) not in di and count == 2:
                di2[(x, y)] = 0

    di = dict(di2)

print(len(di))
