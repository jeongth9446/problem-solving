import math


def chkpow(v):
    k = int(math.sqrt(v))
    if k * k == v:
        return True
    else:
        return False


m = int(input())
n = int(input())

minnum = 0
sumnum = 0
for item in range(m, n + 1):
    if chkpow(item):
        sumnum += item
        if minnum == 0:
            minnum = item

if minnum == 0:
    print(-1)
else:
    print(sumnum)
    print(minnum)
