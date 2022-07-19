import sys

input = sys.stdin.readline

n = int(input())
res = 0

for i in range(n):
    a, b = list(map(int, input().split()))
    res += b % a

print(res)
