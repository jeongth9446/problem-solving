n, m = list(map(int, input().split()))

a = [0 for i in range(n)]
b = [0 for i in range(n)]

for i in range(n):
    t = int(input())
    a[i] = t
    for j in range(n):
        if a[j] >= t and i != j:
            a[j] += 1

for i in range(m, 0, -1):
    t = int(input())
    k = 0
    for j in range(n):
        if a[j] == i:
            b[j] = t
            k = j
    for j in range(n):
        if b[j] >= t and k != j:
            b[j] += 1

for k in range(1, 4):
    for i in range(n):
        if b[i] == k:
            print(i + 1)
