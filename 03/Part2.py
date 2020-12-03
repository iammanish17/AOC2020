s = open('input.txt','r').read()
#s = ''''''
pro = 1
s = [[p for p in k] for k in s.split("\n")]
for p, q in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    i, j = 0, 0
    ans = 0
    while True:
        j += p
        i += q
        j = j % len(s[0])
        try:
            s[i][j]
        except:break
        if s[i][j] == '#':
            ans += 1
    pro *= ans

print(pro)
