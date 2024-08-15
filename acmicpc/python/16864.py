a, b, c = list(map(float, input().split()))
a = int(round(a * 100, 1))
b = int(round(b * 100, 1))
c = int(round(c * 100, 1))

flag = True

for i in range(int(a / b) + 1):

    if a - i * b < 0:
        break
    if int((a - i * b) // c) * c == a - i * b:
        flag = False
        print(i, int((a - i * b) // c))

if flag:
    print("none")
