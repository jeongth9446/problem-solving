k, l = list(map(int, input().split()))

flag = False
res = 0
for i in range(2, l):
    if k % i == 0:
        flag = True
        res = i
        break

if flag:
    print("BAD " + str(res))
else:
    print("GOOD")
