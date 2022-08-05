n, m = list(map(int, input().split()))

res = 0
while n != 0:
    res += n
    n = int(n / m)

print(res)
