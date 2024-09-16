n = int(input())

for i in range(n):
    c, p = list(map(int, input().split()))

    print(c, p)

    print(c * p - 2 * (c - 1))
