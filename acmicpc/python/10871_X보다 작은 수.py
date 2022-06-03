n, x = input().split()
n = int(n)
x = int(x)

arr = input().split()

for item in arr:
    tmp = int(item)
    if tmp < x:
        print(str(tmp) + ' ', end = '')

