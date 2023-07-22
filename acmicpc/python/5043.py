import math

n, b = list(map(int, input().split()))

k = math.pow(2, b + 1) - 1

if n <= k:
    print("yes")
else:
    print("no")