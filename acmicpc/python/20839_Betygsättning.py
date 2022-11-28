x, y, z = list(map(int, input().split()))
a, b, c = list(map(int, input().split()))

flag = 'E'

if c >= z:
    flag = 'E'
    if b * 2 >= y:
        flag = 'D'
    if b >= y:
        flag = 'C'
        if a * 2 >= x:
            flag = 'B'
        if a >= x:
            flag = 'A'
print(flag)
