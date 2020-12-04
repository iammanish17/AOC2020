s = open('input.txt','r').read()
s = [k for k in s.split("\n")]
t = []
field=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
ans=0
for i in s:
    if i == '':
        fields = []
        for p in t:
            for each in p.split(" "):
                fields += [each.split(":")[0]]

        t = []
        b = [k for k in field if k not in fields]
        if len(b) == 0 or (len(b) == 1 and b[0] == 'cid'):
            ans += 1

    else:
        t += [i]
print(ans)
