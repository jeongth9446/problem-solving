n, m = list(map(int, input().split()))

s = list(map(int, input().split()))

t = list()

for _ in range(n):
    t.append(list(map(int, input().split())))

res = [0 for i in range(n+m)]

for idx in range(n):
    res[idx] = s[idx]

for i in range(n):
    for j in range(n+m):
        res[j] += t[i][j]
        res[i] -= t[i][j]

for item in res:
    print(item, end=" ")