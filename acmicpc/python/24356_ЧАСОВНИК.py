t1, m1, t2, m2 = list(map(int, input().split()))

a1 = 60 * t1 + m1
a2 = 60 * t2 + m2

if a1 > a2:
    a2 += 24 * 60

res = a2 - a1

print(res, res // 30)
