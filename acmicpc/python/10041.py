w, h, n = list(map(int, input().split()))
res, a, b = 0, 0, 0

for i in range(n):
    x, y = list(map(int, input().split()))
    if a > 0 and b > 0:
        if (a-x) * (b-y) < 0:
            res += abs(a - x) + abs(b - y)
        else:
            res += max(abs(a - x), abs(b - y))
    a, b = x, y

print(res)
