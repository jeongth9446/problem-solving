n = int(input())


def gcd(x: int, y: int):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


for _ in range(n):
    a, b = list(map(int, input().split()))

    k = gcd(a, b)
    print(a * b // k, k)
