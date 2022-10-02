n = int(input())

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

res = abs(a - c) + abs(b - d)
for _ in range(n - 2):
    x, y = list(map(int, input().split()))
    res += abs(c - x) + abs(d - y)
    c = x
    d = y

res += abs(a - c) + abs(b - d)

print(res)
