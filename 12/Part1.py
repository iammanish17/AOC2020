s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

x, y = 0, 0
cur = 'E'
bb = ['E', 'S', 'W', 'N']

for line in s:
    a, b = line[0], int(line[1:])
    if a == 'E':
        x += b
    if a == 'W':
        x -= b
    if a == 'N':
        y += b
    if a == 'S':
        y -= b
    if a == 'L' or a == 'R':
        if a == 'R':
            cur = bb[(bb.index(cur) + b//90)%4]
        if a == 'L':
            cur = bb[(bb.index(cur) - b//90)%4]
    if a == 'F':
        if cur == 'E':
            x += b
        if cur == 'W':
            x -= b
        if cur == 'N':
            y += b
        if cur == 'S':
            y -= b
print(abs(x) + abs(y))
