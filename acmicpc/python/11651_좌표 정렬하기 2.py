import sys

n = int(sys.stdin.readline())

arr = list()
for t in range(0, n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

for item in arr:
    print(item[0], item[1])

