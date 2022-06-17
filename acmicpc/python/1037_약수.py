import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

max = max(arr)
min = min(arr)

k = max * min

while True:
    flag = 0
    for item in arr:
        if k % item != 0:
            flag = 1

    if flag == 0:
        print(k)
        break
    else:
        k += min
