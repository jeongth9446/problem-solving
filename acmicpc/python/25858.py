n, d = list(map(int, input().split()))

a = list()
s = 0
for i in range(n):
    p = int(input())
    a.append(p)
    s += p

for i in range(n):
    print(int(a[i] * d // s))
