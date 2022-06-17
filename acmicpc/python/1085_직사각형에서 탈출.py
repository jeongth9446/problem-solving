import sys

x, y, w, h = list(map(int, sys.stdin.readline().split()))

res = min(abs(x-w), x, abs(y-h), y)

print (res)