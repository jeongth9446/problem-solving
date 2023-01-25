n = int(input())

a = list(input())
b = list(input())
res = 0

for i in range(len(a)):
    if a[i] != b[i]:
        res += 1
print(len(a)-res)
