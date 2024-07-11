n = int(input())

miny = 10000
minx = 10000
for i in range(n):
    x, y = list(map(int, input().split()))

    if y < miny:
        miny = y
        minx = x

print(minx, miny)