import sys

n = int(input())

arr = list()
for k in range(0, n):
    arr.append(sys.stdin.readline())

arr = sorted(arr, key=lambda x: (len(x), x))

tmp = ""
for item in arr:
    if tmp == item:
        continue
    tmp = item
    print(item, end="")