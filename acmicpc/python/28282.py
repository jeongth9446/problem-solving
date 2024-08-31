x, k = list(map(int, input().split()))

a = list(map(int, input().split()))

lSocks = a[0:x]
rSocks = a[x:]
lCnt = [0 for _ in range(k + 1)]
rCnt = [0 for _ in range(k + 1)]

for i in lSocks:
    lCnt[i] += 1

for i in rSocks:
    rCnt[i] += 1

res = 0

for i in range(k + 1):
    res += lCnt[i] * (x - rCnt[i])

print(res)
