a, b = list(map(int, input().split()))
c = int(input())

m = a + b

if m - 2*c >= 0:
    print(m - 2*c)
else:
    print(m)