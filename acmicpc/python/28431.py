p = [0 for _ in range(10)]
for _ in range(5):
    a = int(input())

    p[a] += 1

for i in range(10):
    if p[i] % 2 == 1:
        print(i)
