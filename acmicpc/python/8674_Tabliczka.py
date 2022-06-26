a, b = list(map(int, input().split()))

d = a // 2
res1 = (a - 2 * d) * b

d = b // 2
res2 = a * (b - 2 * d)

print(min(res1, res2))
