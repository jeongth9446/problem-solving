import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

res = 0
for i in a:
    for j in a:
        res += abs(i-j)

print(res)
