m, n = list(map(int, input().split()))

k = min(m, n)
if m > n:
    print(k * 2 - 1)
else:
    print(k * 2 - 2)
