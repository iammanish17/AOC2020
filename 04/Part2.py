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
                f, v = each.split(":")
                try:
                    if f == 'byr' and 1920 <= int(v) <= 2002:
                        fields += [f]
                    if f == 'iyr' and 2010 <= int(v) <= 2020:
                        fields += [f]
                    if f == 'eyr' and 2020 <= int(v) <= 2030:
                        fields += [f]
                    if f == 'hgt':
                        if v.endswith("cm") and 150<=int(v.replace("cm",""))<=193:
                            fields += [f]
                        if v.endswith("in") and 59<=int(v.replace("in",""))<=76:
                            fields += [f]
                    if f == 'hcl' and v[0] == '#' and len(v) == 7:
                        if sum([int(k in "0123456789abcdef") for k in v[1:]])==6:
                            fields += [f]
                    if f == 'ecl' and v in ['amb', 'blu', 'brn', 'gry','grn', 'hzl', 'oth']:
                        fields += [f]
                    if f == 'pid' and int(v) >= 0 and len(v) == 9:
                        fields += [f]
                except:pass

        t = []
        b = [k for k in field if k not in fields]
        if len(b) == 0 or (len(b) == 1 and b[0] == 'cid'):
            ans += 1

    else:
        t += [i]
print(ans)
