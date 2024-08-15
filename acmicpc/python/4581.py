while True:
    arr = list(input())

    if arr[0] == "#":
        break

    y = 0
    n = 0
    p = 0
    a = 0

    for item in arr:
        if item == "Y":
            y += 1
        if item == "N":
            n += 1
        if item == "P":
            p += 1
        if item == "A":
            a += 1

    tot = y + n + p + a

    if a * 2 >= tot:
        print("need quorum")
    elif y > n:
        print("yes")
    elif n > y:
        print("no")
    else:
        print("tie")
