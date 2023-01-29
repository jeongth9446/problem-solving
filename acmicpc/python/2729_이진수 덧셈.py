n = int(input())


def bin2dec(x: int):
    k = list(str(x))
    k.reverse()
    p = 1
    res = 0
    for item in k:
        if item == '1':
            res += p
        p *= 2
    return res


def dec2bin(x: int):
    s = list()
    p = x

    while p != 0:
        s.append(str(p % 2))
        p = p // 2
    s.reverse()
    if len(s) == 0:
        return "0"
    return "".join(s)


for _ in range(n):
    a, b = list(map(int, input().split()))

    c = bin2dec(a)
    d = bin2dec(b)
    print(dec2bin(c + d))
    # print(c, d)
