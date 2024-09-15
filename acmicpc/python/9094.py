t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    res = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a * a + b * b + m) % (a * b) == 0:
                res += 1
    print(res)
