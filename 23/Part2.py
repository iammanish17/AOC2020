class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

nodes = [-1]*(10**6 + 1)

cur = None
for i in "974618352":
    num = int(i)
    if not cur:
        cur = Node(num)
        nodes[num] = cur
    else:
        next = Node(num)
        next.left = cur
        cur.right = next
        cur = next
        nodes[num] = cur

for i in range(10, 10**6+1):
    next = Node(i)
    next.left = cur
    cur.right = next
    cur = next
    nodes[i] = cur

cur.right = nodes[9]
nodes[9].left = cur

cur = nodes[9]
for i in range(10**7):
    v = cur.value
    x, y, z = cur.right, cur.right.right, cur.right.right.right
    cur.right = z.right
    cur.right.left = cur

    target = v - 1
    if target == 0: target = 10**6
    p = [x.value, y.value, z.value]
    while target in p or (target == cur):
        target -= 1
        if target == 0:
            target = 10**6
    next = nodes[target]
    z.right = next.right
    z.right.left = z
    next.right = x
    x.left = next

    cur = cur.right

print(nodes[1].right.right.value*nodes[1].right.value)
