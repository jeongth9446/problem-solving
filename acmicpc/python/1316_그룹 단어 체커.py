n = int(input())

res = 0
for i in range(0, n):
    dic = dict()
    a = list(input())
    flag = True
    for i in range(0, len(a)):
        if a[i] not in dic:
            dic[a[i]] = True
        elif a[i] == a[i-1]:
            pass
        else:
            flag = False

    if flag:
        res += 1

print(res)