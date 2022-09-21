import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    value, unit = list(map(str, input().split()))

    value = float(value)

    if unit == "kg" :
        print("{0:.4f}".format(value * 2.2046), "lb")
    elif unit == "lb":
        print("{0:.4f}".format(value * 0.4536), "kg")
    elif unit == "l":
        print("{0:.4f}".format(value * 0.2642), "g")
    else:
        print("{0:.4f}".format(value * 3.7854), "l")

