import math

s = int(input())
a = int(input())
b = int(input())

print(max(250, 250 + math.ceil((s - a) / b) * 100))
