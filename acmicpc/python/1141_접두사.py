import sys

input = sys.stdin.readline

n = int(input())

strList = list()
for _ in range(n):
    strList.append(input().strip())

res = list()

# print(strList)

strList.sort(key=lambda x: -len(x) )
# print(strList)

for item in strList:

    flag = 0
    for s in res:
        if str.find(s, item) == 0:
            flag = 1
            break
    if flag == 0:
        res.append(item)

print(len(res))