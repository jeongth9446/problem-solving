a, x, b, y = list(map(int, input().split()))
c, z, d, w = list(map(int, input().split()))

k = max((max(a, b, c, d) - min(a, b, c, d)), max(w, x, y, z) - min(w, x, y, z))

print(k * k)
