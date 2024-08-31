k = int(input())

for i in range(k):
    a = int(input())

    while True:
        a = a + 1
        p = list(str(a)).count('0')

        if (p == 0):
            print(a)
            break
