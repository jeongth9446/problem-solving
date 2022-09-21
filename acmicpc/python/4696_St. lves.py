while True:
    n = float(input())
    if n == 0:
        break
    k = 1
    res = 0
    for _ in range(5):
        res = res + k
        k = k * n

    print("{0:0.2f}".format(res))
