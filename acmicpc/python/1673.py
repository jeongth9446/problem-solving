while True:
    try:
        n, k = list(map(int, input().split()))
        res = 0
        stamp = 0
        while n > 0:
            res += n
            stamp += n
            n = stamp // k
            stamp %= k

        print(res)
    except EOFError:
        break
