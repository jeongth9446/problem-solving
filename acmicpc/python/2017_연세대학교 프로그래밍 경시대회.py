n = int(input())

res = 0

for i in range(1, n):
    for j in range(i+2, n):
        a = i
        b = j
        c = n-i-j
        if c <= 0:
            break
        if c % 2 == 0:
            res += 1

print(res)