s = open('input.txt','r').read()
#s = '''FBFBBFFRLR'''

s = [k for k in s.split("\n")]

ans = 0
for line in s:
    a = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    b  = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    ans = max(ans, a*8+b)
print(ans)
