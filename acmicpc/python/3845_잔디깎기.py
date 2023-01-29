while True:
    nx, ny, w = list(map(float, input().split()))
    if nx == ny == w == 0.0:
        break
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    x.sort()
    y.sort()

    flag = True

    cl = 0.0
    for idx in range(len(x)):
        if x[idx] - w / 2 <= cl:
            cl = x[idx] + w / 2
        else:
            flag = False

    if cl < 75:
        flag = False

    # print(cl)
    cl = 0.0
    for idx in range(len(y)):
        if y[idx] - w / 2 <= cl:
            cl = y[idx] + w / 2
        else:
            flag = False

    if cl < 100:
        flag = False

    # print(cl)
    if flag:
        print("YES")
    else:
        print("NO")
