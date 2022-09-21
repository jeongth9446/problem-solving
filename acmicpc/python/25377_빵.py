import sys

input = sys.stdin.readline

n = int(input())

m = 10000
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a <= b:
        if b < m:
            m = b

if m == 10000:
    print(-1)
else:
    print(m)
