a = list()
for i in range(9):
    a.append(int(input()))

a.sort()

s = sum(a)

for i in range(9):
    for j in range(i + 1, 9):
        if s - a[i] - a[j] == 100:
            for k in range(9):
                if a[k] != a[i] and a[k] != a[j]:
                    print(a[k])
            exit(0)