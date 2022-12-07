n = int(input())

a = list(map(int, input().split()))

v = 0

for ai in a:
    v = 1 - (1-v)*(1-ai/100)
    print(v*100)

