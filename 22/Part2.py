s = open('input.txt','r').read()

s = [k for k in s.split("\n")]
a,b=[], []
aa,bb=False,False
for line in s:
    if "Player 1" in line:
        aa = True
    elif aa and "Player 2" not in line and line:
        a += [int(line)]
    elif aa and "Player 2" in line:
        aa = False
        bb = True
    elif bb and line:
        b += [int(line)]

games = set()
def f(a, b, round):
    if (str(a), str(b), round) in games:
        return a, 1
    games.add((str(a), str(b), round))
    if not a:return b, 2
    if not b:return a, 1
    x, y = a.pop(0), b.pop(0)
    if x <= len(a) and y <= len(b):
        arr, winner = f(a[:x], b[:y], round+1)
        if winner == 1:
            return f(a+[x,y], b, round)
        else:
            return f(a,b+[y,x], round)
    if x > y:
        a += [x, y]
    if y > x:
        b += [y, x]
    return f(a,b, round)

c, w = f(a,b,1)
ind = 1
ans = 0
for i in range(len(c) - 1, -1, -1):
    ans += c[i]*ind
    ind += 1
print(ans)
