D, H, M = list(map(int, input().split()))

k = 11 * 24 * 60 + 11 * 60 + 11

a = D * 24 * 60 + H * 60 + M

if (a < k):
    print(-1)
else:
    print(a - k)