import sys

input = sys.stdin.readline

n = int(input())

for idx in range(1, n + 1):
    a, b, c = list(map(int, input().split()))

    print("Scenario #" + str(idx) + ":")
    if a * a + b * b + c * c == 2 * max(a, b, c) * max(a, b, c):
        print("yes\n")
    else:
        print("no\n")
