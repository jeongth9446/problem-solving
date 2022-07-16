import sys

t = int(input())

input = sys.stdin.readline

for idx in range(1, t + 1):
    a, b, c = list(map(int, input().split()))

    print("Case #" + str(idx) + ": ", end="")
    if a + b + c <= 2 * max(a, b, c):
        print("invalid!")
    elif a == b == c:
        print("equilateral")
    elif a == b or b == c or c == a:
        print("isosceles")
    else:
        print("scalene")
