import math

n = int(input())
res = 100000*100000
resi = 0
resj = 0
for i in range(n+1):
    j = int(math.sqrt(n*n - i*i)) + 1
    k = math.sqrt(i*i + j*j)
    if k > n:
        if k < res:
            res = k
            resi = i
            resj = j
    j = int(math.sqrt(n*n - i*i))
    k = math.sqrt(i*i + j*j)
    if k > n:
        if k < res:
            res = k
            resi = i
            resj = j
print(resi, resj)

