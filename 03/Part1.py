s = open('input.txt','r').read()
#s = ''''''

s = [[p for p in k] for k in s.split("\n")]
i, j = 0, 0
ans = 0
while True:
    j += 3
    i += 1
    j = j % len(s[0])
    try:
        s[i][j]
    except:break
    if s[i][j] == '#':
        ans += 1

print(ans)
