s = list(input())
s = ["".join(s[i] + s[i + 1]) for i in range(0, len(s), 2)]

A = 0
B = 0
flag = 0

for item in s:
    if item == 'A1':
        A += 1
    elif item == 'A2':
        A += 2
    elif item == 'B1':
        B += 1
    elif item == 'B2':
        B += 2

    if flag == 0:
        if A >= 11:
            print("A")
            break
        elif B >= 11:
            print("B")
            break

        if A == B == 10:
            flag = 1
    elif flag == 1:
        if A >= B + 2:
            print("A")
            break
        elif B >= A + 2:
            print("B")
            break
