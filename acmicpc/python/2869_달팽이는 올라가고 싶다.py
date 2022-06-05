import math
import sys

a, b, v = map(int, sys.stdin.readline().split())
print(math.ceil(1 + (v-a)/(a-b)))
