n = int(input())

a = input()

for i in range(len(a)):
    b = a[i:]
    if b.count('t') == b.count('s'):
        print(b)
        exit(0)
