s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

ans = 0

def check(bag):
    for line in s:
        x = line.split(" contain ")
        x[0] = x[0].replace("bags", "bag")
        r = x[1].split(", ")
        if bag in x[0]:
            if "no other bag" in line:return 0
            bn = ["".join(r for r in k if r.isalpha() or r == ' ').replace("bags", "bag")
                  for k in r]
            count = [int("".join(r for r in k if r.isdigit() or r == ' ').replace("bags", "bag"))
                  for k in r]
            total = 0
            for bagname, count in zip(bn, count):
                total += count+check(bagname.strip())*count
            return total
print(check("shiny gold bag"))

