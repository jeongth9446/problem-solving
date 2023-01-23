n, k = list(map(int, input().split()))

s = list(map(int, input().split()))

p = sum(s[0:k])
res = p
for idx in range(k, n):
    # print(p, idx, idx-k)
    p = p + s[idx] - s[idx - k]
    if p > res:
        res = p

print(res)
