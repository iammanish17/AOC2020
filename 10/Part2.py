s = open('input.txt','r').read()

s = [int(k) for k in s.split("\n")]

s = sorted(s)
target = max(s) + 3
s += [target]

di = {}

def f(v):
    if v in di:return di[v]
    if v == target: return 1
    else:
        ans = 0
        if v+1 in s:
            ans += f(v+1)
        if v+2 in s:
            ans += f(v+2)
        if v+3 in s:
            ans += f(v+3)
        di[v] = ans
        return di[v]
print(f(0))
