s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

def invert(a):
    return [k[::-1] for k in a]

def rotate(a):
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0])-1,-1,-1)]
def top(a):
    return a[0]
def bottom(a):
    return a[-1]
def left(a):
    return [k[0] for k in a]
def right(a):
    return [k[-1] for k in a]

di = {}
a = []
id = 0
ok = []
rotations = {}

for line in s:
    if "Tile" in line:
        id = int(line.split(" ")[1][:-1])
    elif id and line:
        a += [[k for k in line]]
    elif id:
        rotations[id] = [a, invert(a)]
        for i in range(3):
            rotations[id] += [rotate(rotations[id][-2])]
            rotations[id] += [invert(rotations[id][-1])]
        di[id] = [a[0], a[-1], [k[0] for k in a], [k[-1] for k in a]]
        for i in range(4):
            di[id] += [di[id][i][::-1]]
        for k in di[id]:
            ok += [k]
        a = []
        id = 0

corners = []
for id in di:
    x = [ok.count(each) for each in di[id]]
    if x.count(1) == 4:
        corners += [id]

keys = [id for id in di]
keys.remove(corners[0])

used = [corners[0]]
cur = None
for i in range(8):
    cur = rotations[used[0]][i]
    if ok.count(top(cur)) == ok.count(left(cur)) == 1:
        break

di2 = {}
di2[used[0]] = cur

while True:
    # make columns
    found = False
    for key in keys:
        for i in range(8):
            if bottom(cur) == top(rotations[key][i]):
                cur = rotations[key][i]
                used += [key]
                di2[used[-1]] = cur
                found = True
                break
        if found:break
    if found:
        keys.remove(used[-1])
    if not found:
        break

arr = []

while keys:
    lefts = list(used)
    for i in lefts:
        row = [i]
        cur = di2[i]
        while True:
            found = False
            for key in keys:
                for i in range(8):
                    if right(cur) == left(rotations[key][i]):
                        cur = rotations[key][i]
                        used += [key]
                        di2[used[-1]] = cur
                        found = True
                        break
                if found:break
            if found:
                row += [used[-1]]
                keys.remove(used[-1])
            else:
                break
        arr += [row]

for x in di2:
    di2[x] = [[di2[x][i][j] for j in range(1, len(di2[x])-1)] for i in range(1, len(di2[x])-1) ]


n = len(di2[used[-1]])

image = [[' ']*(n * len(arr)) for i in range(n * len(arr))]

for i in range(len(arr)):
    for j in range(len(arr)):
        cur = di2[arr[i][j]]
        for k in range(n):
            for l in range(n):
                image[i*n+k][j*n+l] = cur[k][l]

#for i in image:print(*i)

sea_monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

sea_monster = [[j for j in k] for k in sea_monster.split("\n")]

images = [image, invert(image)]
for i in range(3):
    images += [rotate(images[-2])]
    images += [invert(images[-1])]

for image in images:
    monster = [[False]*len(image) for i in range(len(image))]
    for i in range(len(image)-len(sea_monster)+1):
        for j in range(len(image)-len(sea_monster[0])+1):
            pos = True
            for k in range(i, i+len(sea_monster)):
                for l in range(j, j+len(sea_monster[0])):
                    if sea_monster[k-i][l-j] == '#' and image[k][l] != '#':
                        pos = False
                        break
                if not pos:
                    break
            if pos:
                for k in range(i, i + len(sea_monster)):
                    for l in range(j, j + len(sea_monster[0])):
                        if image[k][l] == sea_monster[k-i][l-j] == '#':
                            monster[k][l] = True

    count, mons = 0, 0
    for i in range(len(image)):
        for j in range(len(image)):
            if image[i][j] == '#':
                count += 1
                if monster[i][j]:
                    mons += 1
    if mons:
        print(count - mons)
        quit()
        
