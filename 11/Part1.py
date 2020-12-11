s = open('input.txt','r').read()


s = [[p for p in k] for k in s.split("\n")]
def f(s):
    s2 = [[''] * len(s[0]) for i in range(len(s))]

    for i in range(len(s)):
        for j in range(len(s[0])):
            cur = s[i][j]
            a=[]
            if i > 0:
                a += [s[i-1][j]]
            if i+1 < len(s):
                a += [s[i+1][j]]
            if j > 0:
                a += [s[i][j-1]]
            if j+1 < len(s[0]):
                a += [s[i][j+1]]
            if i > 0 and j>0:
                a += [s[i-1][j-1]]
            if i > 0 and j+1 < len(s[0]):
                a += [s[i-1][j+1]]
            if i+1 < len(s) and j > 0:
                a += [s[i+1][j-1]]
            if i+1 < len(s) and j+1 < len(s[0]):
                a += [s[i+1][j+1]]
            if cur == "L" and a.count("L") + a.count(".") == len(a):
                s2[i][j] = '#'
            elif cur == "#" and a.count("#") >= 4:
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
