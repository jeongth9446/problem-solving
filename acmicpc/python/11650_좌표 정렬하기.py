import sys

n = int(sys.stdin.readline())

arr = list()
for t in range(0, n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x: (x[0], x[1]))

for item in arr:
    print(item[0], item[1])

