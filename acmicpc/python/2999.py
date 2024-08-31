a = input()
a_len = len(a)

x, y = 0, 0

for i in range(1, int(a_len / 2) + 1):
    for j in range(i, a_len + 1):
        if i * j == a_len:
            x, y = i, j

for i in range(x):
    for j in range(y):
        print(a[i + j * x], end='')
