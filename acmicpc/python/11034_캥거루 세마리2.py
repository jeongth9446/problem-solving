while True:
    try:
        a, b, c = list(map(int, input().split()))

        if a + 1 == b:
            print(c - b - 1)
        elif b + 1 == c:
            print(b - a - 1)
        else:
            print(max(c - b - 1, b - a - 1))
    except EOFError:
        break
