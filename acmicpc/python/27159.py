n = int(input())
s = list(map(int, input().split()))

res = 0

for idx in range(n):
    if idx == 0:
        res += s[idx]
    else:
        if s[idx - 1] + 1 != s[idx]:
            res += s[idx]

print(res)
