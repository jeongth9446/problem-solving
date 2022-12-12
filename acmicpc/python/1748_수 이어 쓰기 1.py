n = int(input())

k = 9
l = 1
res = 0

while n > k:
    # print(l, k)
    res += l * k
    l += 1
    n -= k
    k *= 10

res += l * n
print(res)