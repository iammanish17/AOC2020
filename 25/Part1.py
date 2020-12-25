mod = 20201227

c = 10212254
d = 12577395

initial = 7

# 7 ^ k % mod = c
# 7 ^ x % mod = d

x = 1
for i in range(1,mod):
    x = (x*7)%mod
    if x == c:
        k1 = i
    if x == d:
        k2 = i

print(pow(c,k2,mod))
print(pow(d,k1,mod))
