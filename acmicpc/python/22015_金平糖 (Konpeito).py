a, b, c = list(map(int, input().split()))

k = max(a, b, c)

print(k - a + k - b + k - c)
