while True:
    a, b, c = list(map(int, input().split()))

    if a == b == c == 0:
        break
    if a+c == 2 * b:
        print("AP " + str(c+c-b))
    else:
        print("GP " + str(int(c*(c/b))))
