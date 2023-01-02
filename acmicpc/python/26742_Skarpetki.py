s = list(input())

c = 0
b = 0

for i in s:
    if i == 'C':
        c += 1
    else:
        b += 1
print(c // 2 + b // 2)
