n, x = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

w = 0
res = 0

for i in range(n):

    w += b[i]
    if w < a[i]:
        k = a[i] - w
        if k % x == 0:
            p = k // x
        else:
            p = k // x + 1

        if res >= p:
            res -= p
            w += p * x
        else:
            print(-1)
            exit(0)
    p = ((w-a[i]) // x)
    w -= p * x
    res += p


print(res)