s = list(input())

res = 0

for i in s:
    if i == "(":
        res += 1
    elif i == ")":
        res -= 1
    else:
        print(res)
        break
