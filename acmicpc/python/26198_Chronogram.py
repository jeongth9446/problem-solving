import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    res = 0
    k = list(input())

    for item in k:
        if item == 'I':
            res += 1
        elif item == 'V':
            res += 5
        elif item == 'X':
            res += 10
        elif item == 'L':
            res += 50
        elif item == 'C':
            res += 100
        elif item == 'D':
            res += 500
        elif item == 'M':
            res += 1000
    print(res)
