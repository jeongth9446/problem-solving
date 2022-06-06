
prime_set = set()


prime_check = [0] * 10001

for i in range (2, 10001):
    if prime_check[i] == 0:
        prime_set.add(i)
        for j in range(i, 10001, i):
            prime_check[j] = 1

t = int(input())
for _k in range(0, t):
    n = int(input())
    a, b = 0, 0
    diff = 10000
    for item in prime_set:
        if item <= n/2:
            if n - item in prime_set:
                if diff > n - 2*item:
                    a, b = item, n-item
                    diff = n - 2*item

    print(min(a, b), max(a, b))

