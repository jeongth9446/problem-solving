m, s, g = list(map(int, input().split()))
a, b = list(map(float, input().split()))
l, r = list(map(int, input().split()))

res1 = l / a + m / g
res2 = r / b + m / s

# print(res1, res2)
if res1 > res2:
    print("latmask")
else:
    print("friskus")
