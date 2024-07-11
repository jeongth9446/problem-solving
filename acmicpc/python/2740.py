n, m = list(map(int, input().split()))

a = list()

for i in range(n):
    a.append(list(map(int, input().split())))

m, k = list(map(int, input().split()))

b = list()

for i in range(m):
    b.append(list(map(int, input().split())))

c = [[0 for _ in range(k)] for _ in range(n)]

#print(c)

for i in range(n):
    for j in range(k):
        p = 0
        for ii in range(m):
            #print(i, j, ii)
            p += a[i][ii] * b[ii][j]
        c[i][j] = p

for i in c:
    for k in i:
        print(k, end=" ")
    print()