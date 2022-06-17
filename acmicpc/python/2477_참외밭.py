import collections

k = int(input())

dir = list()
amount = list()

h = 0
w = 0
m = 0

dir_cnt = collections.defaultdict(int)

for i in range(0, 6):
    a, b = list(map(int, input().split()))

    dir.append(a)
    amount.append(b)

    if (a == 1 or a == 2) and w < b:
        w = b
    if (a == 3 or a == 4) and h < b:
        h = b

# print(w, h)
dir.append(dir[0])
amount.append(amount[0])

for i in range(0, 6):
    t = [dir[i], dir[i + 1]]
    tmount = [amount[i], amount[i + 1]]

    # print(t)
    if t == [1, 3] or t == [3, 2] or t == [2, 4] or t == [4, 1]:
        m = tmount[0] * tmount[1]
        break

print((h * w - m) * k)
