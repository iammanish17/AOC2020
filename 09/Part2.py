s = open('input.txt','r').read()
#s=''''''

s = [int(k) for k in s.split("\n")]

target = 756008079

total = [0]
for i in range(len(s)):
    total += [total[-1] + s[i]]

for k in total:
    if target + k in total:
        rang = s[total.index(k):total.index(target+k)]
        print(min(rang) + max(rang))
        quit()
