import math
import sys

cnt = 0
input = sys.stdin.readline
while True:
    a, b, c = list(map(int, input().split()))
    if a == b == c == 0:
        break
    cnt += 1

    print("Triangle #" + str(cnt))

    if c == -1:
        print("c =", "{0:.3f}".format(math.sqrt(a*a + b*b)))
    elif a == -1:
        t = c*c - b*b
        if t <= 0:
            print("Impossible.")
        else:
            print("a =", "{0:.3f}".format(math.sqrt(t)))
    elif b == -1:
        t = c * c - a * a
        if t <= 0:
            print("Impossible.")
        else:
            print("b =", "{0:.3f}".format(math.sqrt(t)))
    print()