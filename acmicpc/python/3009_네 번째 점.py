import sys

x1, y1 = list(map(int, sys.stdin.readline().split()))
x2, y2 = list(map(int, sys.stdin.readline().split()))
x3, y3 = list(map(int, sys.stdin.readline().split()))

if x1 != x2 and x2 == x3 and x3 != x1:
    x4 = x1

if y1 != y2 and y2 == y3 and y3 != y1:
    y4 = y1

if x1 != x2 and x2 != x3 and x3 == x1:
    x4 = x2

if y1 != y2 and y2 != y3 and y3 == y1:
    y4 = y2

if x1 == x2 and x2 != x3 and x3 != x1:
    x4 = x3

if y1 == y2 and y2 != y3 and y3 != y1:
    y4 = y3

print(x4, y4)