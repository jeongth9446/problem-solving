n = int(input())

for i in range(1, n + 1):
    a, b = list(map(int, input().split()))

    print("Scenario #" + str(i) + ":")
    print((a + b) * (b - a + 1) // 2)
    print()
