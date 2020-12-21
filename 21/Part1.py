s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

aller = {}
count = {}

for line in s:
    allergens = line.split("contains ")[1].split(", ")
    allergens[-1] = allergens[-1][:-1]
    ing = line.split(" (")[0].split(" ")
    for i in ing:
        count[i] = 1 if i not in count else count[i] + 1
    for allergen in allergens:
        if allergen not in aller:
            aller[allergen] = set(ing)
        else:
            aller[allergen] = aller[allergen].intersection(set(ing))

used = set()
while True:
    found = False
    for allergen in aller:
        aller[allergen] = aller[allergen].difference(used)
        if len(aller[allergen]) == 1:
            used.add(list(aller[allergen])[0])
            found = True
            break
    if not found:break

ans = 0
for x in count:
    if x not in used:
        ans += count[x]
        #print(x,count[x])
print(ans)
