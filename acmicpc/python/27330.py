import collections

n = int(input())
a = list(map(int, input().split()))
m = int(input())

b = list(map(int, input().split()))

res = 0

m = collections.defaultdict(int)
for i in b:
    m[i] = 1

for item in a:
    res += item
    if m[res] != 0:
        res = 0

print(res)
