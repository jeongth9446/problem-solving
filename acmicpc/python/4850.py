while True:
    try:
        n, w, d, g = map(int, input().split())
        ws = n * (n - 1) // 2 * w
        x = (ws - g) // d

        if x != 0:
            print(x)
        else:
            print(n)
    except:
        break
