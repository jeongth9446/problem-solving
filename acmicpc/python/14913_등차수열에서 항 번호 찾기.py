a, d, k = list(map(int, input().split()))

n = int((k - a) / d + 1)

if a + (n - 1) * d == k and n > 0:
    print(n)
else:
    print("X")
