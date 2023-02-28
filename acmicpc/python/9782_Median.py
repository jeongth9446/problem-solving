cnt = 0
while True:
    cnt += 1
    a = list(map(int, input().split()))

    if a[0] == 0:
        break

    s = a[1:]

    if a[0] % 2 == 1:
        print("Case " + str(cnt) + ": " + "{0:.1f}".format(s[a[0] // 2]))
    else:
        print("Case " + str(cnt) + ": " + "{0:.1f}".format((s[a[0] // 2] + s[a[0] // 2 - 1]) / 2))
