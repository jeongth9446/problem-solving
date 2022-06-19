import sys

n, m = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

s = 0
acc = list()
acc.append(0)
for item in arr:
    s += item
    acc.append(s)


for i in range(0, m):
    a, b = list(map(int, sys.stdin.readline().split()))

    print(acc[b] - acc[a-1])
