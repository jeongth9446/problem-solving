import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, d, a, b, f = list(map(float, input().split()))

    print(int(n), d / (a + b) * f)
