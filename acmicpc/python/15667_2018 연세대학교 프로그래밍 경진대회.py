k = int(input())

for i in range(1, 101):
    if i + i * i + 1 == k:
        print(i)
        exit(0)
