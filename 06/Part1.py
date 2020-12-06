s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

ans = 0
p = ""
for line in s:
    if line == "":
        x = [0]*26
        for i in p:
            j = ord(i) - 97
            if 0 <= j < 26:
                x[j] = 1
        ans += sum(x)
        p = ""
    else:
        p += line
print(ans)
