def dec2b(v: int, q: int):
    x = v
    s = list()
    while x != 0:
        s.append(str(x % q))
        x = x // q

    s.reverse()
    if len(s) == 0:
        return "0"
    return "".join(s)


def b2dec(v: str, q: int):
    x = list(v)
    x.reverse()
    res = 0
    i = 1
    for item in x:
        res += int(item) * i
        i *= q
    return res


while True:
    s = input()

    if s == '0':
        break

    b, p, m = list(map(str, s.split()))
    b = int(b)
    p = b2dec(p, b)
    m = b2dec(m, b)

    k = p % m
    print(dec2b(k, b))
