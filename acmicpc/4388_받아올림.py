while True:
    a, b = list(map(int, input().split()))

    if a == 0 and b == 0:
        break

    a = list(map(int, str(a)))
    b = list(map(int, str(b)))
    a.reverse()
    b.reverse()

    for _ in range(11-len(a)):
        a.append(0)
    for _ in range(11 - len(b)):
        b.append(0)

#    print(a, b)

    res = 0
    carry = 0
    for idx in range(11):
        if a[idx] + b[idx] + carry >= 10:
            res += 1
            carry = 1
        else:
            carry = 0

    print(res)
