import sys

input = sys.stdin.readline

n = int(input())

resa = resb  = 100

for _ in range(n):
    a, b = list(map(int, input().split()))
    if a > b:
        resb -= a
    elif a < b:
        resa -= b

print(resa)
print(resb)