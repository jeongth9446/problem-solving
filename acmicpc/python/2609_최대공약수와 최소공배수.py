n, m = list(map(int, input().split()))

for i in range(10000, 0, -1):
    if m % i == 0 and n % i == 0:
        print(i)
        print(int(m*n/i))
        break