s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

def f(s2):
    vis = set()
    acc = 0
    i = 0
    while i < len(s2):
        if i in vis:
            return False
        vis.add(i)
        if "acc" in s2[i]:
            acc += int(s2[i][4:])
            i += 1
        elif "jmp" in s2[i]:
            i += int(s2[i][4:])
        else:
            i += 1
    return acc

for i in range(len(s)):
    if "jmp" in s[i]:
        s2 = list(s)
        s2[i] = s2[i].replace("jmp", "nop")
        if f(s2):
            print(f(s2))

    elif "nop" in s[i]:
        s2 = list(s)
        s2[i] = s2[i].replace("nop", "jmp")
        if f(s2):
            print(f(s2))
