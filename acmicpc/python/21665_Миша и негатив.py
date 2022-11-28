n, m = list(map(int, input().split()))

l = list()
k = list()
for _ in range(n):
    l.append(list(input()))

input()

for _ in range(n):
    k.append(list(input()))

res = 0

for i in range(n):
    for j in range(m):
        if l[i][j] == k[i][j]:
            res += 1

print(res)