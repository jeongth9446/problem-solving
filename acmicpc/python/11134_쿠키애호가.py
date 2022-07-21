import math
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, c = list(map(int, input().split()))

    print(math.ceil(n / c))
