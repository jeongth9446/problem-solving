import sys

n = int(input())


def gcd(a: int, b: int):
    if b % a == 0:
        return a
    else:
        return gcd(b%a, a)


for i in range(0, n):
    a, b = list(map(int, sys.stdin.readline().split()))

    print(int(a * b / gcd(a, b)))
