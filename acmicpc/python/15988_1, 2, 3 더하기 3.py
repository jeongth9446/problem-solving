# 15988 1, 2, 3 더하기 3
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    a, b, c = 1, 2, 4

    for k in range(n - 1):
        a, b, c = b, c, (a + b + c) % 1000000009

    print(a)
