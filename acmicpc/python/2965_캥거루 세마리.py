a, b, c = list(map(int, input().split()))

k = max(b - a, c - b)
print(k - 1)
