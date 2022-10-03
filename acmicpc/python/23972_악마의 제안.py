a, b = list(map(int, input().split()))

if b == 1:
    print(-1)
else:
    if a * b % (b - 1) == 0:
        res = a * b // (b - 1)
    else:
        res = (a * b // (b - 1)) + 1
    print(res)
