import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    _ = input()

    n, m = list(map(int, input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = max(a)
    b = max(b)

    if a >= b:
        print("S")
    else:
        print("B")
