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
    bi = bin(int(index))[2:]
    bi = "0"*(36 - len(bi)) + bi
    x = ['X']*36
    oof = []
    for i in range(36):
        if mask[i] == '0':
            x[i] = bi[i]
        elif mask[i] == '1':
            x[i] = '1'
        else:
            oof += [i]
    values = []
    if oof:
        for i in range(2**len(oof)):
            xx = list(x)
            bi = bin(i)[2:]
            bi = "0"*(len(oof)-len(bi))+bi
            for j in range(len(oof)):
                xx[oof[j]] = bi[j]
            values += [int("".join(xx),2)]
    else:
        values += [int("".join(x), 2)]
        
    for v in values:
        di[v] = value

print(sum(di[k] for k in di))
