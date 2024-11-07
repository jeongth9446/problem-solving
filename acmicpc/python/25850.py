p = int(input())

c = list()
for i in range(p):
    k = list(map(int, input().split()))[1:]
    for j in k:
        c.append([chr(ord('A')+i), j])

c.sort(key = lambda x: (x[1]))

for i in c:
    print(i[0], end="")