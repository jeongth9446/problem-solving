import math

w, h = list(map(int, input().split()))

print(w + h - math.sqrt(w * w + h * h))
