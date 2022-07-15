while True:

    try:
        a, b = list(map(int, input().split()))
        print(int(b / (a + 1)))
    except EOFError:
        break
