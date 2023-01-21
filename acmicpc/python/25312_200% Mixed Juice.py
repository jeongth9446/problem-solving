def gcd(x: int, y: int):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


n, m = list(map(int, input().split()))

juice = list()
for i in range(n):
    juice.append(list(map(int, input().split())))

# print(juice)

juice.sort(key=lambda x: [-(x[1] / x[0])])

# print(juice)

a = 0
b = 1

M = 0
idx = 0

while M + juice[idx][0] < m:
    M += juice[idx][0]
    a += juice[idx][1]
    idx += 1

b = juice[idx][0]
a *= b

a += juice[idx][1] * (m - M)

# print(a, b)

c = gcd(a, b)

print(str(a // c) + "/" + str(b // c))
