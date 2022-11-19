l, h = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    k = int(input())
    res = min(1000, k) * l + max(0, k - 1000) * h
    print(k, res)
