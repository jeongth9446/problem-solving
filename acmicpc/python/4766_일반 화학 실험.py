k = float(input())

while True:
    t = float(input())

    if t == 999:
        break
    print("{0:.2f}".format(t - k))
    k = t