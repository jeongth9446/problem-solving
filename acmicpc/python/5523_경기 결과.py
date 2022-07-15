import sys

n = int(input())

resa, resb = 0, 0
for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))

    if a > b:
        resa += 1
    elif b > a:
        resb += 1

print(resa, resb)