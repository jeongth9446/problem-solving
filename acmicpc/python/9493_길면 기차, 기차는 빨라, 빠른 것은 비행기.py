import sys

input = sys.stdin.readline

while True:
    M, A, B = list(map(int, input().split()))

    if M == A == B == 0:
        break

    tA, tB = M / A * 3600, M / B * 3600

    tGap = abs(tA - tB)

    print(str(int(tGap / 3600)) + ":" + "{0:02d}".format(int(tGap % 3600 / 60)) + ":" + "{0:02d}".format(
        round(tGap % 60)))
