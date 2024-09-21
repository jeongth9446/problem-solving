n = int(input())

for i in range(n):
    a, b, c = list(map(int, input().split()))
    x, y, z = a, b, c
    while c:
        c -= 1
        if a > b:
            a //= 2
        else:
            b //= 2

    print("Data set:", x, y, z)
    print(max(a, b), min(a, b))
    print()
