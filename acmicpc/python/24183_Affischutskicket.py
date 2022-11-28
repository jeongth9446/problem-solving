a, b, c = list(map(int, input().split()))
a /= 1000 * 1000
b /= 1000 * 1000
c /= 1000 * 1000

res = 229 * 324 * a * 2 + 297 * 420 * b * 2 + 210 * 297 * c
print(res)
