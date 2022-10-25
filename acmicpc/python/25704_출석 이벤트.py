n = int(input())
p = int(input())
res = p
if n >= 5:
    res = min(res, p - 500)
# print(p)
if n >= 10:
    res = min(res, int(p * 0.9))
# print(p)
if n >= 15:
    res = min(res, p - 2000)
# print(p)
if n >= 20:
    res = min(res, int(p * 0.75))
# print(p)

res = max(0, res)

print(res)
