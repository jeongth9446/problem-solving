n = int(input())

for _ in range(n):
    k = int(input())
    res = 0
    for _ in range(k):
        a, b, c = list(map(str, input().split()))
        b = int(b)
        c = float(c)
        res += b * c
    print("$" + format(res, ".2f"))
