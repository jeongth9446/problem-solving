import sys

n, m, k = list(map(int, sys.stdin.readline().split()))

print(k // m, k % m)
