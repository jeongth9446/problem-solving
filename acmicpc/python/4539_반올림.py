# 4539 반올림

n = int(input())

for _ in range(n):
    k = int(input())
    p = 1
    while k > p * 10:
        if k % (p * 10) >= p * 5:
            k = ((k // (p * 10)) + 1) * (p * 10)
        else:
            k = (k // (p * 10)) * (p * 10)
        p *= 10

    print(k)
