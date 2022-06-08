import sys

n = int(sys.stdin.readline())

arr = [0]*10001

for i in range(0, n):
    t = int(sys.stdin.readline())
    arr[t] += 1

for i in range(1, 10001):
    for k in range(0, arr[i]):
        print(i)
