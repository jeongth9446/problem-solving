n = int(input())

res = 0
for _ in range(n):
    h, b, k = list(map(int, input().split()))

    res += max(0, b - h) * k

print(res)
