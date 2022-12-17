t = int(input())

for _ in range(t):
    n = int(input())
    in_arr = list(map(int, input().split()))
    d_arr = [0 for _ in range(1001)]
    res = min(in_arr)
    for i in range(0, n):
        d_arr[i] = in_arr[i]
        if in_arr[i] + d_arr[i - 1] > d_arr[i]:
            d_arr[i] = in_arr[i] + d_arr[i - 1]
        res = max(d_arr[i], res)

    print(res)
