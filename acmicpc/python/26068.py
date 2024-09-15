n = int(input())

res = 0
for i in range(n):
    a = input()
    a = a.replace("D-", "")
    if (int(a) <= 90):
        res += 1

print(res)
