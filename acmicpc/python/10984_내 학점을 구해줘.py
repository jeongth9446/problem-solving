import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    res1 = res2 = 0

    for _ in range(n):
        a, b = list(map(float, input().split()))
        res1 += a
        res2 += a*b

    res2 /= res1

    print(int(res1), res2)

