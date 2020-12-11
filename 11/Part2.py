s = open('input.txt','r').read()

s = [[p for p in k] for k in s.split("\n")]
def f(s):
    s2 = [[''] * len(s[0]) for i in range(len(s))]

    for i in range(len(s)):
        for j in range(len(s[0])):
            cur = s[i][j]
            a=[]
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if not k and not l:continue
                    p, q = i, j
                    while 0 <= p+k < len(s) and 0 <= q + l < len(s[0]):
                        p, q = p+k, q+l
                        if s[p][q] == '#' or s[p][q] == 'L':
                            a += [s[p][q]]
                            break
            if cur == "L" and a.count("L") + a.count(".") == len(a):
                s2[i][j] = '#'
            elif cur == "#" and a.count("#") >= 5:
                s2[i][j] = "L"
            else:
                s2[i][j] = cur
    return s2

s2=[]
while True:
    s2 = f(s)
    if str(s2) == str(s):
        break
    s = [list(k) for k in s2]


print(str(s).count("#"))
