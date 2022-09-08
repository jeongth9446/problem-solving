l = int(input())
r = int(input())

res = 0
k = 2
l = int(l*r/100)
while True:
    # print(l)
    if l <= 5:
        break
    res += l * k
    l = int(l * r / 100)
    k *= 2


print(res)
