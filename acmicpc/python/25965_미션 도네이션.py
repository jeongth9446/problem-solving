n = int(input())
for _ in range(n):
    m = int(input())
    s = list()
    for _ in range(m):
        s.append(list(map(int, input().split())))

    k, d, a = list(map(int, input().split()))

    res = 0
    for item in s:
        if item[0] * k - item[1] * d + item[2] * a > 0:
            res += item[0] * k - item[1] * d + item[2] * a

    print(res)
