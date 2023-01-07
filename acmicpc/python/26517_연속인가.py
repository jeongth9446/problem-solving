k = int(input())

a, b, c, d = list(map(int, input().split()))

res1 = a * k + b
res2 = c * k + d

if res1 == res2:
    print("Yes", res1)
else:
    print("No")
