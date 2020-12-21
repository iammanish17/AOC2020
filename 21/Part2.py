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
match = {}
while True:
    found = False
    for allergen in aller:
        aller[allergen] = aller[allergen].difference(used)
        if len(aller[allergen]) == 1:
            match[allergen] = list(aller[allergen])[0]
            used.add(list(aller[allergen])[0])
            found = True
            break
    if not found:break

x = sorted([k for k in match])
print(",".join(match[k] for k in x))
