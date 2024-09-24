n = int(input())

for i in range(n):
    x = int(input())

    res = 0
    for j in range(x):
        a, b, c = list(map(str, input().split()))
        b = int(b)
        c = float(c)

        res += b * c

    print("$" + "%.2f" %res)
