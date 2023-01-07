n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))

    for _ in range(b):
        for _ in range(a):
            print("X", end="")
        print()
    print()
    