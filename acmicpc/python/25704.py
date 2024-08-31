n = int(input())

p = int(input())

res = p

if n >= 5:
    res = min(res, p - 500)
if n >= 10:
    res = min(res, int(p * 0.9))
if n >= 15:
    res = min(res, p - 2000)
if n >= 20:
    res = min(res, int(p * 0.75))

print(max(res, 0))
