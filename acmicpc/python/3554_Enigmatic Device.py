import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    j, l, r = list(map(int, input().split()))
    if j == 1:
        for idx in range(l-1, r):
            a[idx] = pow(a[idx], 2) % 2010
        # print(a)
    elif j == 2:
        print(sum(a[l-1: r]))

