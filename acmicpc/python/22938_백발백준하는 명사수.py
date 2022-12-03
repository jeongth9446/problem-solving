import math

x1, y1, r1 = list(map(int, input().split()))
x2, y2, r2 = list(map(int, input().split()))

d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

if r1 + r2 <= d:
    print("NO")
else:
    print("YES")
