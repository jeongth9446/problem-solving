n = int(input())
lst = list(map(int, input().split()))

odd = 0
even = 0

for item in lst:
    if item % 2 == 0:
        even += 1
    else:
        odd += 1

res = 0
if n % 2 == 1 and odd - 1 == even:
    res = 1
if n % 2 == 0 and odd == even:
    res = 1

print(res)
