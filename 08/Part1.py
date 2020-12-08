s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

vis = set()
i = 0
acc = 0
while i < len(s):
    if i in vis:
        print(acc)
        quit()
    vis.add(i)
    if "acc" in s[i]:
        acc += int(s[i][4:])
        i += 1
        continue
    elif "jmp" in s[i]:
        i += int(s[i][4:])
        continue
    else:
        i += 1
        continue
