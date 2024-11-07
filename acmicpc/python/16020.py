n = int(input())

a = list()

for i in range(n):
    a.append(list(map(int, input().split())))

# print(a)

p = 100000000000
pr = 0
pc = 0
q = 0
qr = 0
qc = 0

for i in range(n):
    for j in range(n):
        if p > a[i][j]:
            p = a[i][j]
            pr, pc = i, j
        if q < a[i][j]:
            q = a[i][j]
            qr, qc = i, j

for i in range(n):
    for j in range(n):
        if (pr, pc) == (0, 0) and (qr, qc) == (n - 1, n - 1):
            print(a[i][j], end=" ")
        elif (pr, pc) == (0, n - 1) and (qr, qc) == (n - 1, 0):
            print(a[j][n - i - 1], end=" ")
        elif (pr, pc) == (n - 1, 0) and (qr, qc) == (0, n - 1):
            print(a[n - j - 1][i], end=" ")
        else:
            print(a[n - i - 1][n - j - 1], end=" ")
    print()
