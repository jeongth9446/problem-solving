import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    res = 0

    for _ in range(n):
        v, f, c = list(map(int, input().split()))
        if d <= v * (f/c):
            res += 1

    print(res)