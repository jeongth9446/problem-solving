a, b, c = list(map(int, input().split()))

print(a + b + c - max(a, b, c) - min(a, b, c))
