s = open('input.txt','r').read()

s = [k for k in s.split("\n")]

x, y = 0, 0
cur = 'E'
bb = ['E', 'S', 'W', 'N']
wx, wy = 10, 1

for line in s:
    a, b = line[0], int(line[1:])
    if a == 'E':
        wx += b
    if a == 'W':
        wx -= b
    if a == 'N':
        wy += b
    if a == 'S':
        wy -= b
    if a == 'L' or a == 'R':
        if a == 'R':
            for i in range(b//90):
                wx, wy = wy, -wx
        if a == 'L':
            for i in range(b//90):
                wx, wy = -wy, wx
    if a == 'F':
        x += b*wx
        y += b*wy
print(abs(x) + abs(y))
