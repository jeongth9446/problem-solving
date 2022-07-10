import math

while True:
    B, N = list(map(int, input().split()))

    if B == 0 and N == 0:
        break

    k = round(math.pow(B, 1/N))

    a = abs(pow(k, N) - B)
    b = abs(pow(k-1, N) - B)
    c = abs(pow(k+1, N) - B)

    res = 0
    dif = 999999

    if dif > a:
        dif = a
        res = k
    if dif > b:
        dif = b
        res = k-1
    if dif > c:
        dif = c
        res = k+1

    print(res)
