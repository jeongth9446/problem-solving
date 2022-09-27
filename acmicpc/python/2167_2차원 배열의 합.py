n, m = list(map(int, input().split()))

a = list()

for _ in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    i, j, x, y = list(map(int, input().split()))

    res = 0

    for p in range(i-1, x):
        for q in range(j-1, y):
            res += a[p][q]

    print(res)
