
cnt = 0

while True:
    a, b, c = list(map(float, input().split()))

    if b == 0:
        exit()

    cnt += 1

    k = round((a * b * 3.1415927) / 5280 / 12, 2)

    m = round(((a * b * 3.1415927) / 5280 / 12) * 60*60 / c, 2)
    print("Trip #" + str(cnt) + ":", "{0:0.2f}".format(k), "{0:0.2f}".format(m))
