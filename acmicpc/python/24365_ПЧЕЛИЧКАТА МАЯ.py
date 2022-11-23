a, b, c = list(map(int, input().split()))

k = (a + b + c) // 3

res = 0

if a < k:
    res = k - a
    b -= res
elif a > k:
    res = a - k
    b += res

if b < k:
    res += k - b
elif b > k:
    res += b - k

print(res)
