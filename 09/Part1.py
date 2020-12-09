s = open('input.txt','r').read()
#s=''''''

s = [int(k) for k in s.split("\n")]


for i in range(25, len(s)):
    pos = False
    for j in range(i-1, i-26, -1):
        for k in range(i-1, i-26, -1):
            if s[j]+s[k] == s[i]:
                pos = True
                break
        if pos:break
    if not pos:
        print(s[i])
