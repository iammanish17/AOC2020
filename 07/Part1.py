s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

ans = 0
p = []
q = []
class K:
    bags=[]
def check(bag):
    for line in s:
        x = line.split(" contain ")
        x[0] = x[0].replace("bags", "bag")
        r = x[1].split(", ")
        if bag in x[1] and x[0] not in K.bags:
            K.bags += [x[0]]
            bn = ["".join(r for r in k if r.isalpha() or r == ' ').replace("bags", "bag")
                  for k in r]
            check(x[0])
check("shiny gold bag")
print(len(K.bags))

