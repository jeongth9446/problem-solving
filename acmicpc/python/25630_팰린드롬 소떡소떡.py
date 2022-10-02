n = int(input())

a = list(input())
b = a.copy()
b.reverse()

res = 0

for idx in range(len(a)):
    if a[idx] != b[idx]:
        res += 1

print(res // 2)