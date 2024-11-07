n = int(input())

res = 0
ti, di = 0, 0
for i in range(n):
    t, d = list(map(int, input().split()))

    if t != 0:
        if res < (d - di) // (t - ti):
            res = (d - di) // (t - ti)
    ti, di = t, d
print(res)
