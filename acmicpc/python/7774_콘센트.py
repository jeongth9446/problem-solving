n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

resa = 1
resb = 0

ap = 0
bp = 0

res = 0
while True:
    flag = 0
    if resb > 0 and bp < len(b):
        resb -= 1
        resa += b[bp]
        bp += 1
        flag = 1
    elif resa > 0 and ap < len(a):
        resa -= 1
        resb += a[ap]
        ap += 1
        flag = 1

    if flag == 0:
        break
    res = max(resa, res)

print(res)