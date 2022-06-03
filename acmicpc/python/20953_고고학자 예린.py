import sys


def dolmen(a: int, b: int) -> int:
    return int((a + b) * (((a + b) * (a + b - 1)) / 2))

t = int(input())

for i in range(0, t):
    a, b = map(int, sys.stdin.readline().split())
    print(dolmen(a, b))