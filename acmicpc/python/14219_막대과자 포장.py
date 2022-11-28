n, m = list(map(int, input().split()))

n %= 3
m %= 3

if n % 3 == 0 or m % 3 == 0:
    print("YES")
else:
    print("NO")
