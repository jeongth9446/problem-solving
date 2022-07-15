import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

max = m

for _ in range(n):
    a, b = list(map(int, input().split()))

    m += a-b

    if m < 0:
        print(0)
        exit()

    if max < m:
        max = m

print(max)