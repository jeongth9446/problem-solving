import sys

input = sys.stdin.readline
t = 0
while True:
    t += 1
    n0 = int(input())
    if n0 == 0:
        break

    n1 = 3 * n0

    if n1 % 2 == 0:
        n2 = n1 // 2
        oe = "even"
    else:
        n2 = (n1 + 1) // 2
        oe = "odd"

    n3 = 3 * n2

    n4 = n3 // 9

    print(str(t) + "." + " " + oe + " " + str(n4))
