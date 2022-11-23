n = int(input())
s = list(input())
res = 0

for item in s:
    if item == 'a' or item == 'i' or item == 'u' or item == 'e' or item == 'o':
        res += 1

print(res)
