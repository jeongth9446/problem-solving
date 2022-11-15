n, a, b, c, d = list(map(int, input().split()))

res1 = 0
res2 = 0
pay1 = 0
pay2 = 0
while res1 < n:
    res1 += a
    pay1 += b
while res2 < n:
    res2 += c
    pay2 += d

print(min(pay1, pay2))
