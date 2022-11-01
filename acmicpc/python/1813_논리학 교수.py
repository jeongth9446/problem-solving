import collections

n = int(input())

res = -1
zero_flag = False

s = collections.defaultdict(int)

k = list(map(int, input().split()))

for item in k:
    s[item] += 1

# print(s)

for key, value in s.items():
    # print(key, value)
    if key == value:
        if res < key:
            res = key
    if key == 0:
        zero_flag = True

if res == -1 and not zero_flag:
    print(0)
else:
    print(res)
