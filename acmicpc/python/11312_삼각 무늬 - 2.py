import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    A, B = list(map(int, input().split()))

    k = int(A / B)

    print(int(k * 1 + 2 * (k * (k - 1) / 2)))
