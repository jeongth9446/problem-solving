while True:

    a, b, c, d = list(map(int, input().split()))
    res = 0

    if a == b == c == d == 0:
        break
    while not (a == b == c == d):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        res += 1

    print(res)
