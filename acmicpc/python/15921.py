n = int(input())

if n == 0:
    print("divide by zero")
else:
    m = list(map(int, input().split()))
    if sum(m) == 0:
        print("divide by zero")
    else:
        print("1.00")
