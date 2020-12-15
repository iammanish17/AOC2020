a = [5,2,8,16,18,0,1]

i = 0

while True:
    if i < len(a):
        i += 1
    else:
        if 1:
            if a.count(a[-1]) >= 2:
                j=len(a)-1
                k=j-1
                while a[k] != a[j]:
                    k -= 1
                a += [j-k]
            else:
                a += [0]
        i += 1
    if len(a) > 2500:break

print(a[2019])
