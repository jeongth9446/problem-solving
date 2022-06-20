n, m = list(map(int, input().split()))


def count2(n: int) -> int:
    res = 0
    while n >= 2:
        res += int(n/2)
        n = int(n/2)
    return int(res)


def count5(n: int) -> int:
    res = 0
    while n >= 5:
        res += int(n/5)
        n = int(n/5)
    return int(res)


print(min(count2(n) - count2(n-m) - count2(m), count5(n) - count5(n-m) - count5(m)))
