import sys

t = int(sys.stdin.readline())

while t > 0:
    t -= 1
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(a+b)
