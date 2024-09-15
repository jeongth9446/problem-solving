n = int(input())

for _ in range(n):
    a = input()

    if a[-1] == '.':
        print(a)
    else:
        print(a + ".")
