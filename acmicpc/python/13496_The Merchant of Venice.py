import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    print("Data Set " + str(i + 1) + ":")
    n, s, d = list(map(int, input().split()))

    sd = s * d
    res = 0
    for _ in range(n):
        d, v = list(map(int, input().split()))
        if d <= sd:
            res += v

    print(res)
    print()
