n = int(input())

a = list()
a.append(1)
for _ in range(n):
    for idx in range(len(a)):
        k = a[idx] % 2
        a[idx] = int(a[idx] / 2)
        if idx < len(a) - 1:
            a[idx + 1] += k * 10
    a.append(5)

for idx in range(len(a)):
    print(a[idx], end="")
    if idx == 0:
        print(".", end="")
