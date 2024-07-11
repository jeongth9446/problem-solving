t = int(input())

ml = [0, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(t):
    y, m = list(map(int, input().split()))

    if m == 1:
        print(str(y-1), str(12), str(31))
    elif m == 3:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            print(str(y), str(m-1), str(29))
        else:
            print(str(y), str(m - 1), str(28))
    else:
        print(str(y), str(m-1), str(ml[m-1]))
