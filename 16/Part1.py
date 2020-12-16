s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

nums = set()
ok = False
ans = 0
for line in s:
    for each in line.split(" "):
        if "-" in each:
            x, y = each.split("-")
            x, y = int(x), int(y)
            for i in range(x,y+1):nums.add(i)
    if "nearby tickets" in line:
        ok = True
    elif ok:
        x = map(int, line.split(","))
        for i in x:
            if i not in nums:
                ans += i
print(ans)
