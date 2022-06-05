a = list()

a.append(list())
for i in range(1, 15):
    a[0].append(i)

for j in range(1, 15):
    a.append(list())
    for i in range(1, 15):
        a[j].append(sum(a[j-1][0:i]))

t = int(input())

for _t in range(0, t):
    k = int(input())
    n = int(input())

    print(a[k][n-1])
