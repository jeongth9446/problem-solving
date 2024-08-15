x = 0
res = ""
for _ in range(7):
    a, b = input().split()
    if x < int(b):
        x = int(b)
        res = a

print(res)
