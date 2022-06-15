import collections
import sys

n = sys.stdin.readline().strip()

arr_n = list(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline().strip()

arr_m = list(map(int, sys.stdin.readline().split()))

dict_n = collections.defaultdict(int)

for item in arr_n:
    dict_n[item] += 1

for item in arr_m:
    print(dict_n[item],end=" ")