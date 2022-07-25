import sys

input = sys.stdin.readline

h, m, s = list(map(int, input().split()))

q = int(input())

for _ in range(q):
    k = list(map(int, input().split()))

    if k[0] == 3:
        print(h, m, s)
    else:
        k[1] %= 24 * 60 * 60 # s가 음수가 되지 않도록 반복 회전에 대해 나머지 처리
        if k[0] == 1:
            s += k[1]
        else:
            s += 24 * 60 * 60 - k[1]

    if s >= 60:
        m += int(s / 60)
        s %= 60
    if m >= 60:
        h += int(m / 60)
        m %= 60
    if h >= 24:
        h %= 24
