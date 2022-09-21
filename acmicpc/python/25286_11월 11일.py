t = int(input())

for _ in range(t):
    y, m = list(map(int, input().split()))

    yun = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

    d = [0, 31, 29 if yun else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m == 1:
        print(y-1, 12, 31)
    else:
        print(y, m-1, d[m-1])

