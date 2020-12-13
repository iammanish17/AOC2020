s = open('input.txt','r').read()


line = [k for k in s.split("\n")]


n = int(line[0])

res = [10**50, -1]

for x in line[1].split(","):
    if x.isdigit():
        y = int(x)
        p = y * ((n+(y-1)) // y)
        if p < res[0]:
            res[0] = p
            res[1] = y
print((res[0] - n)*res[1])
