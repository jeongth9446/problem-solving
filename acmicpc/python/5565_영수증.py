import sys

input = sys.stdin.readline

res = int(input())

for _ in range(9):
    res -= int(input())

print(res)
