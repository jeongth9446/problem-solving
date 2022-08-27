import collections

s1, s2, s3 = list(map(int, input().split()))

dic = collections.defaultdict(int)
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            dic[i + j + k] += 1

# print(dic)

lst = list()

for key, value in dic.items():
    lst.append([key, value])

# print(lst)

lst.sort(key=lambda x: (-x[1], x[0]))

print(lst[0][0])
