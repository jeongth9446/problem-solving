import math

n = int(input())

for i in range(n):
    a1, p1 = list(map(int, input().split()))
    r1, p2 = list(map(int, input().split()))

    p = a1 / p1
    q = r1 * r1 * math.pi / p2

    if p < q:
        print("Whole pizza")
    else:
        print("Slice of pizza")
