a = [5,2,8,16,18,0,1]

i = 0

di = [-1]*(3*10**7)
for i in range(len(a)):
    di[a[i]] = i

b, a = 0, 1
while True:
    if i < 7:
        i += 1
    else:
        di[b] = i - 2
        b = a
        if 1:
            if di[a] != -1:
                a = i-1-di[a]
            else:
                a = 0

        i += 1
    if i > 3*(10**7):break

print(b)
