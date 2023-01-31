n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))

    res = 0
    if a == 0:
        pass
    else:
        if a <= 1:
            res += 500
        elif a <= 3:
            res += 300
        elif a <= 6:
            res += 200
        elif a <= 10:
            res += 50
        elif a <= 15:
            res += 30
        elif a <= 21:
            res += 10

    if b == 0:
        pass
    else:
        if b <= 1:
            res += 512
        elif b <= 3:
            res += 256
        elif b <= 7:
            res += 128
        elif b <= 15:
            res += 64
        elif b <= 31:
            res += 32

    print(res * 10000)
