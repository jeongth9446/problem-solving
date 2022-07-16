import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    s = list(map(int, input().split()))

    res = 0

    for item in s:
        res += int(item/k)

    print(res)