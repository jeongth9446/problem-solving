import math

n, w, h = list(map(int, input().split()))

d = math.sqrt(pow(w, 2) + pow(h, 2))

for _ in range(n):
    t = int(input())
    if t <= d:
        print("DA")
    else:
        print("NE")
