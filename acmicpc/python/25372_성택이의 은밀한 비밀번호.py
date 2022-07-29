import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    t = input().strip()

    if (6 <= len(t) <= 9):
        print("yes")
    else:
        print("no")
