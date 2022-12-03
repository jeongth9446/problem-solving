a = list(input())
b = list(map(str, input().split()))

for item in a:
    flag = 0
    for k in b:
        if item == k:
            print(item.lower(), end="")
            flag = 1
    if flag == 0:
        print(item, end="")
       