a, b = list(map(int, input().split()))

arr = [0 for item in range(100001)]

arr[1] = 1
arr[0] = 1
prime = list()
for i in range(2, 100000):
    if arr[i] == 0:
        for j in range(i*2, 100000, i):
            arr[j] = 1

for k in range(100000):
    if arr[k] == 0:
        prime.append(k)

s = set()

for item in prime:
    s.add(item)

res = 0
for i in range(a, b+1):
    p = 0
    q = i
    if i in s:
        continue
    for l in prime:
        if q in s:
            p += 1
            break
        while q % l == 0:
            q = q // l
            p += 1

    if p in s:
        res += 1

print(res)