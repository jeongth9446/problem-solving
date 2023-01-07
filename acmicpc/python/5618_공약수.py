def gcd(x: int, y: int):
    if y == 0:
        return x
    return gcd(y, x % y)


n = int(input())

a = list(map(int, input().split()))

r = a[0]

r = gcd(r, a[1])

if n == 3:
    r = gcd(r, a[2])

for i in range(1, r + 1):
    if r % i == 0:
        print(i)
