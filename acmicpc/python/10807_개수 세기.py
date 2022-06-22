import collections

n = int(input())

arr = list(map(int, input().split()))

v = int(input())

cnt = collections.Counter(arr)

print(cnt[v])
