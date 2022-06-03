t = int(input())

for looping in range(0, t):
    a, b = input().split()
    a = int(a)
    b = list(b)
    for i in b:
        print(i * a, end='')
    print()