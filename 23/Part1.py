x = [int(k) for k in "974618352"]

u = 0
for j in range(100):
    cur = x[u%9]
    target = cur - 1
    p = [x[(u+k+1)%9] for k in range(3)]
    if target == 0:target = 9
    while target in p or target==cur:
        target -= 1
        if target == 0:
            target = 9
    for each in p:
        x.remove(each)
    ind = x.index(target)
    x.insert(ind+1, p[0])
    x.insert(ind + 2, p[1])
    x.insert(ind + 3, p[2])
    u = (x.index(cur)+1)%9
print(*x[(x.index(1)+1):]+x[:x.index(1)],sep='')
