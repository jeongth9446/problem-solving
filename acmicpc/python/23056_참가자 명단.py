n, m = list(map(int, input().split()))

k = list()
d = [0 for i in range(n + 1)]
while True:
    s = input().split()
    if s[0] == "0" and s[1] == "0":
        break
    if d[int(s[0])] >= m:
        pass
    else:
        k.append([int(s[0]), s[1]])
        d[int(s[0])] += 1

k.sort(key=lambda x: [x[0] % 2 != 1, x[0], len(x[1]), x[1]])

for item in k:
    print(item[0], item[1])
