import sys

n, k = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))
acc = list()
acc.append(0)
s = 0

for item in arr:
    s += item
    acc.append(s)

maxx = -100000000

for i in range(k, n+1):
    # print(i, i -k, acc[i], acc[i-k])
    if acc[i] - acc[i-k] > maxx:
        maxx = acc[i] - acc[i-k]

print(maxx)