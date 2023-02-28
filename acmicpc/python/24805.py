a, b, c = list(map(int, input().split()))

res = 0

h = 0

while h <= c:
    res += 1
    h += a
    if h >= c:
        break
    h -= b

print(res)
