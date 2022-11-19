n, d = list(map(int, input().split()))

l = list()
for _ in range(n):
    l.append(int(input()))

for item in l:
    print(d // sum(l) * item)
