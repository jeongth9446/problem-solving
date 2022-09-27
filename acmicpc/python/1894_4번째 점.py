while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = list(map(float, input().split()))
        ax = x1
        ay = y1
        if x2 == x3 and y2 == y3:
            ax = x1
            ay = y1
            bx = x4
            by = y4
            cx = x3
            cy = y3
        elif x2 == x4 and y2 == y4:
            ax = x1
            ay = y1
            bx = x3
            by = y3
            cx = x4
            cy = y4
        elif x1 == x3 and y1 == y3:
            ax = x2
            ay = y2
            bx = x4
            by = y4
            cx = x1
            cy = y1
        else:
            ax = x2
            ay = y2
            bx = x3
            by = y3
            cx = x1
            cy = y1

        dx = cx - bx
        dy = cy - by
        resx = ax - dx
        resy = ay - dy

        print("{0:0.3f}".format(resx), "{0:0.3f}".format(resy))

    except EOFError:
        break
