n = int(input())

res = 0

for i in range(n):
    w, h = list(map(int, input().split()))

    res = max(res, w * h)

print(res)
