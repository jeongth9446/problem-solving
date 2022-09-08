a = list(map(int, input().split()))

res = 5000

for item in a:
    if item == 1:
        res -= 500
    elif item == 2:
        res -= 800
    elif item == 3:
        res -= 1000

print(res)