import sys

while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))

    if a == b == c == 0:
        break

    heru = max(a, b, c)

    if a*a + b*b + c*c == 2 * heru*heru:
        print("right")
    else:
        print("wrong")