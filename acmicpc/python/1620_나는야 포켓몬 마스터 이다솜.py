import collections
import sys

n, m = list(map(int, sys.stdin.readline().split()))

dict_num2eng = collections.defaultdict(str)
dict_eng2num = collections.defaultdict(int)

for i in range(n):
    t = sys.stdin.readline().strip()

    dict_eng2num[t] = i+1
    dict_num2eng[i+1] = t

for i in range(m):
    t = sys.stdin.readline().strip()

    if t.isnumeric():
        print(dict_num2eng[int(t)])
    else:
        print(dict_eng2num[t])
