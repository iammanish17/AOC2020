s = open('input.txt','r').read()


s = [k for k in s.split("\n")]

rules = [[]for i in range(500)]
rules[47] = ["a"]
rules[84] = ["b"]

f = [[]for i in range(500)]
for line in s:
    r = line.split(":")[0]
    if r.isdigit():
        r = int(r)
        pos = [[int(p) for p in k.split(" ") if p.isdigit()] for k in line.split(":")[1].split("|")]
        pos = [k for k in pos if k]
        f[r] = pos
    else:
        break

from itertools import product
def fun(x):
    if rules[x]:return rules[x]
    ans = []
    for k in f[x]:
        xx = []
        for i in k:
            xx += [fun(i)]
        ans += ["".join(k for k in list(o)) for o in product(*xx)]
    rules[x] = ans
    return rules[x]

for i in range(500):
    if f[i]:
        fun(i)
r0 = set(rules[0])
ans = 0
for line in s:
    if line in r0:
        ans += 1

print(ans)
