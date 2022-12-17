x, n = list(map(int, input().split()))

if x < 0 and n == 1:
    print("INFINITE")
elif x >= 0 and n == 1:
    print("0")
elif n % 2 == 1:
    print("ERROR")
elif x <= 0:
    print("0")
elif n == 0:
    print("INFINITE")
else:
    n = n // 2
    print((x + n - 1) // n - 1)
