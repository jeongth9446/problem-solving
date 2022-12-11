
n = int(input())


def f(k, p, q):
    if k == 0:
        return

    f(k - 1, p, 6 - p - q)
    print(p, q)
    f(k - 1, 6 - p - q, q)


print(pow(2, n) - 1)
if n <= 20:
    f(n, 1, 3)
