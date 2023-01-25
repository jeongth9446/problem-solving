z = int(input())

for _ in range(z):
    r, g, b = 0, 0, 0

    for _ in range(10):
        i, j, k = list(map(int, input().split()))
        r += i
        g += j
        b += k

    r = int(r / 10 + 0.5)
    g = int(g / 10 + 0.5)
    b = int(b / 10 + 0.5)
    print(r, g, b)
