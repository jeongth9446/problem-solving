n = int(input())
m = int(input())

if n >= 6:
    print("Love is open door")
else:
    for idx in range(n-1):
        if idx % 2 == 0:
            print(1-m)
        else:
            print(m)
