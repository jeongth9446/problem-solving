while True:
    n = int(input())
    if n == 0:
        break

    k = list()

    for _ in range(n):
        k.append(input())

    k.sort(key=lambda x: x.upper())

    print(k[0])
