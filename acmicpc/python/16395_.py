n, k = list(map(int, input().split()))

a = list()

a.append(list())

a[0].append(1)
a.append([1,1])
for i in range(2, n):
    a.append(list())

    a[i].append(1)
    for j in range(1, i):
        a[i].append(a[i-1][j-1] + a[i-1][j])
    a[i].append(1)

print(a[n-1][k-1])