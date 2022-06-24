a, b = list(map(int, input().split()))

if (a + b) % 2 != 0 or (a - b) % 2 != 0 or (a - b) < 0:
    print(-1)
else:
    print((a + b) // 2, abs((a - b) // 2))
