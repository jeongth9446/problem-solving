in_arr = list(input().lower())

dic = dict()

for item in in_arr:
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

dic = sorted(dic.items(),key= lambda x: x[1], reverse=True)

if len(dic) == 1 or dic[0][1] != dic[1][1]:
    print(dic[0][0].upper())
else:
    print("?")
