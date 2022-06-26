import collections

t = int(input())
arr = list(map(int, input().split()))
print(collections.Counter(arr)[t])
