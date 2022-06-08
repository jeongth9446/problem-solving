import sys

n = int(sys.stdin.readline())

arr = list()
for k in range(0, n):
    t = list(map(str, sys.stdin.readline().split()))
    arr.append([int(t[0]), t[1], k])

arr = sorted(arr, key=lambda x:(x[0], x[2]))

for item in arr:
    print(item[0], item[1])