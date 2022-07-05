a, b = list(map(int, input().split()))

m = (b - a) / 400

res = 1 / (1 + pow(10, m))

print(res)
