import collections
import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

dic = collections.defaultdict(int)
for _ in range(m):
    a, b = list(map(int, input().split()))
    dic[a] += 1
    dic[b] += 1

for idx in range(1, n+1):
    print(dic[idx])