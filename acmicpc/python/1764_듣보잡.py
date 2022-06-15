import collections
import sys

n, m = list(map(int, input().split()))

dict_n = collections.defaultdict(int)
list_res = list()

for i in range(n):
    dict_n[sys.stdin.readline().strip()] = 1

for i in range(m):
    t = sys.stdin.readline().strip()
    if dict_n[t] == 1:
        list_res.append(t)

list_res = sorted(list_res)

print(len(list_res))
for item in list_res:
    print(item)