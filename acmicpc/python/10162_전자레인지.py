t = int(input())

if t % 10 != 0:
    print("-1")
else:

    # 5분 : 300초, 1분 : 60초, 10초 : 10초

    res1 = res2 = res3 = 0

    while t >= 300:
        t -= 300
        res1 += 1
    while t >= 60:
        t -= 60
        res2 += 1
    while t >= 10:
        t -= 10
        res3 += 1

    print(res1, res2, res3)