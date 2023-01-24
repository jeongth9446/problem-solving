n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))
    c = bin(a)[2:].count('1')
    if c % 2 == b:
        print("Valid")
    else:
        print("Corrupt")
