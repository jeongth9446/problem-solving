import sys

input = sys.stdin.readline

n = int(input())

res = 0
for i in range(n):
    res += int(input())

print(res - n + 1)
