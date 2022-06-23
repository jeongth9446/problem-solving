import sys

while True:
    a, b = list(map(int, sys.stdin.readline().split()))

    if a == b == 0:
        exit()
    if(a <= b):
        print("No")
    else:
        print("Yes")