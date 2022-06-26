a, b = list(map(int, input().split()))

if a * (100-b)*0.01 < 100:
    print(1)
else:
    print(0)