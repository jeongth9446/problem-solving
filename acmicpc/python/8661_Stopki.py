x, k, a = list(map(int, input().split()))

x = x % (k + a)

if x < k:
    print(1)
else:
    print(0)
