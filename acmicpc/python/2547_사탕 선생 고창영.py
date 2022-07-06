import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    tmp = input()
    res = 0
    n = int(input())
    for k in range(n):
        res += int(input())

    if res % n == 0:
        print("YES")
    else:
        print("NO")
