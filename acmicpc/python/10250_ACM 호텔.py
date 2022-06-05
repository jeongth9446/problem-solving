import math

t = int(input())

for _t in range(0, t):
    h, w, n = map(int, input().split())

    if n % h != 0:
        a = n % h
    else:
        a = h

    b = math.ceil(n/h)

    print(str(a) + "{0:02d}".format(b))

