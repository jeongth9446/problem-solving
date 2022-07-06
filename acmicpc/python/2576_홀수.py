arr = list()
res = 0

for i in range(7):
    t = int(input())
    if t % 2 == 1:
        res += t
        arr.append(t)

if len(arr) == 0:
    print("-1")
else:
    print(res)
    print(min(arr))