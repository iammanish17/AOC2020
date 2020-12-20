s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

di = {}
a = []
id = 0
ok = []
for line in s:
    if "Tile" in line:
        id = int(line.split(" ")[1][:-1])
    elif id and line:
        a += [[k for k in line]]
    elif id:
        di[id] = [a[0], a[-1], [k[0] for k in a], [k[-1] for k in a]]
        for i in range(4):
            di[id] += [di[id][i][::-1]]
        for k in di[id]:
            ok += [k]
        a = []
        id = 0

ans = 1
for id in di:
    x = [ok.count(each) for each in di[id]]
    if x.count(1) == 4:
        ans *= id

print(ans)
