n, m = list(map(int, input().split()))

k = [[i + 1, 0] for i in range(m)]

for _ in range(n):
    t = list(map(int, input().split()))
    for i in range(m):
        k[i][1] += t[i]

# print(k)

k.sort(key=lambda x: -x[1])

for i in range(m):
    print(k[i][0], end=" ")
