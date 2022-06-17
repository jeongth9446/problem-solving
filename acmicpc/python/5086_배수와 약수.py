import sys

while True:
    n, m = list(map(int, sys.stdin.readline().split()))

    if n == m == 0:
        break

    if n % m == 0:
        print("multiple")
    elif m % n == 0:
        print("factor")
    else:
        print("neither")