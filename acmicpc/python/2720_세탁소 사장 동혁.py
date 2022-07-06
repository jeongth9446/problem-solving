t = int(input())

for i in range(t):
    n = int(input())

    a, b, c, d = 0, 0, 0, 0

    while n >= 25:
        a += 1
        n -= 25
    while n >= 10:
        b += 1
        n -= 10
    while n >= 5:
        c += 1
        n -= 5
    while n >= 1:
        d += 1
        n -= 1

    print(a, b, c, d)

