n = int(input())

a = list()

for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort()

res = 0
c = 10001

for i in a:
    if i[1] < c:
        c = i[1]
        res += 1

print(res)
