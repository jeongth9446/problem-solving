while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break

    res = 1
    for i in range(1, arr[0]+1):
        res *= arr[i*2 - 1]
        res -= arr[i*2]

    print(res)
    