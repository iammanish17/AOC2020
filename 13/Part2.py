s = open('input.txt','r').read()


line = [k for k in s.split("\n")]


n = int(line[0])

res = [10**50, -1]

l2= [int(k) if k != "x" else 1 for k in line[1].split(",")]


def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1):
        return 0

    # Apply extended Euclid Algorithm
    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t

        # Make x1 positive
    if (x1 < 0):
        x1 = x1 + m0

    return x1


# k is size of num[] and rem[].
# Returns the smallest
# number x such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[]
# are pairwise coprime
# (gcd for every pair is 1)
def findMinX(num, rem, k):
    # Compute product of all numbers
    prod = 1
    for i in range(0, k):
        prod = prod * num[i]

        # Initialize result
    result = 0

    # Apply above formula
    for i in range(0, k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp

    return result % prod

n = []
a = []

for i in range(len(l2)):
    x = l2[i]
    n += [int(x)]
    a += [(n[-1]-i)%n[-1]]
print(findMinX(n, a, len(n)))
