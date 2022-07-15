import sys

input = sys.stdin.readline


def fact(n: int):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


while True:
    n = int(input())

    if n == 0:
        break
    a = list(map(int, list(str(n))))
    res = 0
    for k in range(len(a), 0, -1):
        res += fact(k) * a[len(a) - k]

    print(res)
