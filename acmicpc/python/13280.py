while True:
    n = int(input())

    if n == 0:
        break

    a = list(map(int, input().split()))

    a.sort()

    res = 1000000

    prev = 1000000
    for item in a:
        res = min(res, abs(prev - item))
        prev = item

    print(res)
