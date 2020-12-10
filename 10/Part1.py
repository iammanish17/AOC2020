s = open('input.txt','r').read()


s = [int(k) for k in s.split("\n")]

s = sorted(s)

cur = 0
one, three = 0, 0
for i in s:
    if i == cur+1:
        one += 1
        cur = i
    elif i == cur+2:
        cur=i
    elif i == cur+3:
        three += 1
        cur=i
print(one*(three+1))
