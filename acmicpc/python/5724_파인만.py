import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    res = 0
    for k in range (n+1):
        res += k*k

    print(res)
