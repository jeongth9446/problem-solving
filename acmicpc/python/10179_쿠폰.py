import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = float(input())

    print("${0:.2f}".format(a * 0.8))
