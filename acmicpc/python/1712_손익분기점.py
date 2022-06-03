import math
a, b, c = map(int, input().split())
if c == b:
    print (-1)
else:
    res = math.floor(float(a) / float(c-b) + 1)
    if res <= 0: res = -1
    print(res)