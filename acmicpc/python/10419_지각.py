import math

t = int(input())

for _ in range(t):
    n = int(input())

    print(int((-1+math.sqrt(1+4*n))/2))