a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for idx in range(3):
    res += max(0, b[idx] - a[idx])

print(res)
