n, m, k = list(map(int, input().split()))

res = 0

while n >= 2 and m >= 1 and n + m >= k:
    res += 1
    n -= 2
    m -= 1

if n + m < k:
    print(res - 1)
else:
    print(res)
