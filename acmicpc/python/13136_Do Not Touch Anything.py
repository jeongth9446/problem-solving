import math

r, c, n = list(map(int, input().split()))

k = r / n
l = c / n
print(math.ceil(k) * math.ceil(l))
