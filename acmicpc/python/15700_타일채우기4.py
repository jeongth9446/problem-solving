n, m = list(map(int, input().split()))

x = int(n / 2)
y = int(m / 2)

res = x * y * 2

if m % 2 == 1:
    res += int(n / 2)
if n % 2 == 1:
    res += int(m / 2)

print(res)
