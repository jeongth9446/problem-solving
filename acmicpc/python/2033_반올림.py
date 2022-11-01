n = int(input())
k = len(str(n))

p = 10

for _ in range(k):
    if n > p:
        if n % p >= p / 2:
            n = (n // p + 1) * p
        else:
            n = (n // p) * p
        p *= 10
    else:
        break

print(n)
