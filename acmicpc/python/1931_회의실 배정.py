import sys

input = sys.stdin.readline

a = list()

n = int(input())

for i in range(0, n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: (x[1], x[0]))

last = 0
res = 0
for i in range(0, n):
    t = a[i]
    if t[0] >= last:
        res += 1
        last = t[1]

print(res) 