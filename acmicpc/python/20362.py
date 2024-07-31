n, a = list(map(str, input().split()))

n = int(n)

b = list()

x = ''
for i in range(n):
    b.append(list(map(str, input().split())))
    if b[i][0] == a:
        x = b[i][1]

res = 0

for i in range(n):
    if b[i][1] == x:
        res += 1
    if b[i][0] == a:
        break

print(res -1)