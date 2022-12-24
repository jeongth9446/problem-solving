import math

n = int(input())

for _ in range(n):
    a1, p1 = list(map(int, input().split()))
    r1, p2 = list(map(int, input().split()))

    res1 = p1 / a1
    res2 = p2 / (r1*r1*math.pi)

    if res1 > res2:
        print("Whole pizza")
    else:
        print("Slice of pizza")