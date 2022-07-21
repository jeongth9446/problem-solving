import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    c, v = list(map(int, input().split()))

    print("You get {0:d} piece(s) and your dad gets {1:d} piece(s).".format(int(c/v), c%v))

