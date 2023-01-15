n, k = list(map(int, input().split()))

res = list()

fk = k % 10
f2k = (k * 2) % 10

for i in range(1, n + 1):
    if i % 10 != fk and i % 10 != f2k:
        res.append(i)

print(len(res))
for i in res:
    print(i, end=" ")
print()

