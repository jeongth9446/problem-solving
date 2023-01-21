n, m = list(map(int, input().split()))

print(min((n - 1) * m + (m - 1), (m - 1) * n + (n - 1)))
