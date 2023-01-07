n = int(input())

for _ in range(n):
    a, b, c = list(map(int, input().split()))

    print("Data set:", a, b, c)

    for _ in range(c):
        if a > b:
            a = a // 2
        else:
            b = b // 2

    print(max(a, b), min(a, b))
    print()
