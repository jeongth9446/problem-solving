import collections

s = list(input())

lst = collections.defaultdict(int)

for i in s:
    lst[i] = 1

# print(lst)

for i in range(ord('A'), ord('Z') + 1):
    if lst[chr(i)] == 0:
        print(chr(i))
