n = list(map(int, input().split()))

res = 0

for item in n:
    res += item * item

print(res % 10)
