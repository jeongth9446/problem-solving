n, t = list(map(int, input().split()))

t = t % (n * 4 - 2)

if 0 < t <= 2 * n:
    print(t)
elif t == 0:
    print(2)
else:
    print(4 * n - t)
