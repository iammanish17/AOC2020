s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

di = {}
ok = False
ans = 0

f = [set() for i in range(20)]
nums = set()
cnt = 0
for line in s:
    for each in line.split(" "):
        if "-" in each:
            x, y = each.split("-")
            x, y = int(x), int(y)
            if line.split(":")[0] not in di:
                di[line.split(":")[0]] = set()
            key = line.split(":")[0]
            for i in range(x,y+1):
                nums.add(i)
                di[key].add(i)
            for i in range(20):
                f[i].add(key)
    if "nearby tickets" in line:
        ok = True
    elif ok:
        x = list(map(int, line.split(",")))
        pos=True
        for i in x:
            if i not in nums:
                pos=False
                break
        if not pos:continue
        for i in range(20):
            st = set()
            for key in di:
                if x[i] in di[key]:
                    st.add(key)
            #print(st)
            f[i] = f[i].intersection(st)
    elif not ok and len(line.split(",")) == 20:
        my = list(map(int, line.split(",")))


st = set()
ind = {}
for j in range(20):
    for i in range(20):
        f[i] = f[i].difference(st)
        if len(f[i]) == 1:
            for k in f[i]:
                ind[k] = i
                st.add(k)
            break
ans = 1
for title in ind:
    if "departure" in title:
        ans *= my[ind[title]]
print(ans)
