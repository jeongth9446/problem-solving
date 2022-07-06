import sys

input = sys.stdin.readline

p = 0
res = 0

for i in range(10):
    a, b = list(map(int, input().split()))
    p += b - a
    res = max(p, res)

print(res)

