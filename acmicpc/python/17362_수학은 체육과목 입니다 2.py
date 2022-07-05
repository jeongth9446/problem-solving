n = int(input())

m = n % 8

if m <= 4 and m != 0:
    print(m)
else:
    if m == 0:
        print(2)
    else:
        print(10 - m)
