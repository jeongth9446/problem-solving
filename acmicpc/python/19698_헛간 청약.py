n, w, h, l = list(map(int, input().split()))

print(min(n, (w // l) * (h // l)))
