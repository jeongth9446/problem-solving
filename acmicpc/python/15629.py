n = int(input())

res = 0
flag1 = False
flag2 = False
flag3 = False

for _ in range(n):
    a = input()

    if a == "ethiopia" or a == "kenya" or a == "tanzania":
        res += 50

    if a == "namibia":
        if flag1:
            res += 40
        else:
            res += 140
    if a == "south-africa":
        flag1 = True
    if a == "zambia":
        flag2 = True
        if flag3:
            res += 20
        else:
            res += 50
    if a == "zimbabwe":
        flag3 = True
        if not flag2:
            res += 30

    if a != "zambia" and a != "zimbabwe":
        flag2 = False
        flag3 = False

print(res)
