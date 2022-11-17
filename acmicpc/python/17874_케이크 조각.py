n, h, v = list(map(int, input().split()))

print(max(h, n - h) * max(v, n - v) * 4)
