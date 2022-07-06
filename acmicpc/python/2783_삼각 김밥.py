import sys

input = sys.stdin.readline

a, b = list(map(int, input().split()))

m = a / b * 1000

n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))
    m = min(a / b * 1000, m)

print("{0:0.2f}".format(m))
