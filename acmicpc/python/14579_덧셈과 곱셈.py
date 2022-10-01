a, b = list(map(int, input().split()))

res = 1

for n in range(a, b + 1):
    r = (n * (n + 1) // 2) % 14579
    res = (res * r) % 14579

print(res)
