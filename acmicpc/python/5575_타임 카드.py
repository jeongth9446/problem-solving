for i in range(0, 3):
    arr = list(map(int, input().split()))

    start = arr[0] * 3600 + arr[1] * 60 + arr[2]
    end = arr[3] * 3600 + arr[4] * 60 + arr[5]

    res = end - start

    print(res // 3600, (res % 3600) // 60, res % 60)
