n = int(input())

res = 0
for b in range(1, 500+1):
    for a in range(b, 500 + 1):
        # print(a, b)
        if a*a == b*b + n:
            res += 1

print(res)