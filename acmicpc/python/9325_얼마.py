import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    res = int(input())

    n = int(input())

    for i in range(n):
        q, p = list(map(int, input().split()))

        res += q * p

    print(res)
