import sys

k = set()
n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr2 = list()
arr3 = dict()

for item in arr:
    k.add(item)

for item in k:
    arr2.append(item)

arr2 = sorted(arr2)

for i, item in enumerate(arr2):
    arr3[item] = i

for item in arr:
    print(arr3[item], end=" ")