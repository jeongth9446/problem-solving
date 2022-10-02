t = int(input())

res = t*t / 4

if res + 0.5 >= res + 1:
    res = int(res) + 1
else:
    res = int(res)

print(res)