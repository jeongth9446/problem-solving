import sys

input = sys.stdin.readline
a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))
a4, b4 = list(map(int, input().split()))

res = 0
p = a1

p += b1
res = max(res, p)
p -= a2
p += b2
res = max(res, p)
p -= a3
p += b3
res = max(res, p)
p -= a4
p += a4
res = max(res, p)

print(res)
