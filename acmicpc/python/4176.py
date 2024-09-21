while True:
    k = input()

    if k == "END":
        break

    res = 0
    k = list(k)

    while True:
        res += 1
        a = k
        k = list(str(len(k)))
        if a == k :
            break

    print(res)
