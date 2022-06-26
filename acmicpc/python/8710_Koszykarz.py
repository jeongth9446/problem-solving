k, w, m = list(map(int, input().split()))

a = w - k

if a % m == 0:
    print(a // m)
else:
    print(a // m + 1)
