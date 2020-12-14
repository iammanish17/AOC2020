s = open('input.txt','r').read()

line = [k for k in s.split("\n")]

mask = line[0].split(" ")[2]

di = {}

for i in line[1:]:
    if "mask" in i:
        mask = i.split(" ")[2]
        continue
    index = i.split("[")[1].split("]")[0]
    value = int(i.split(" ")[2])
    bi = bin(value)[2:]
    bi = "0"*(36 - len(bi)) + bi
    x = ['0']*36
    for i in range(36):
        if mask[i] == 'X':
            x[i] = bi[i]
        else:
            x[i] = mask[i]
    x = int("".join(x), 2)
    di[index] = x

print(sum(di[k] for k in di))
