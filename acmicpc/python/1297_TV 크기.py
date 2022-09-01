import math

d, h, w = list(map(int, input().split()))

k = math.sqrt((d * d) / (h * h + w * w))

print(int(h * k), int(w * k))
