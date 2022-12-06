n, m, k = list(map(int, input().split()))

p = k - 3

m = (m + p - 1) % n + 1
print(m)
