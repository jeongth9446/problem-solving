n = int(input())

p = list()
k = 0

for i in range(n):
    a, b = list(map(str, input().split()))

    if a == 'jinju':
        print(b)
        k = int(b)

    p.append(int(b))

res = 0

for i in p:
    if i > k:
        res += 1

print(res)