import sys

input = sys.stdin.readline

k = int(input())
n = int(input())
ta = 0
for _ in range(n):
    t, z = input().split()
    t = int(t)

    if ta + t < 210:
        ta += t
        if z == "T":
            k += 1
        if k == 9:
            k = 1
    else:
        print(k)
        break
