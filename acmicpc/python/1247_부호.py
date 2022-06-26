import sys

input = sys.stdin.readline

for t in range(0, 3):
    n = int(input())
    res = 0
    for i in range(0, n):
        res += int(input())
    if res > 0:
        print("+")
    elif res < 0:
        print("-")
    else:
        print("0")

