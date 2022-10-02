import math

b, c = list(map(int, input().split()))

b *= 2

u = int((-b + math.sqrt(b*b - 4 * c))//2)
v = int((-b - math.sqrt(b*b - 4 * c))//2)

if u < v:
    print(u, v)
elif u > v:
    print(v, u)
else:
    print(v)