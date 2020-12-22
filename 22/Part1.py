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

while max(len(a), len(b)) != len(a)+len(b):
    x, y = a.pop(0), b.pop(0)
    if x > y:
        a += [x, y]
    else:
        b += [y, x]

c = a + b
ind = 1
ans = 0
for i in range(len(c) - 1, -1, -1):
    ans += c[i]*ind
    ind += 1
print(ans)
