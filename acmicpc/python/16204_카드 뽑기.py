n, m, k = list(map(int, input().split()))

print(min(m, k) + min(n-m, n-k))
