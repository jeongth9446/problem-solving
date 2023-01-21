import math

n = int(input())

k = math.sqrt(n)
k_int = int(math.sqrt(n))

if k == k_int:
    print(max(4 * (k_int - 1), 4))
else:
    if (k_int + 1) * k_int > n:
        print(max(2 * (2 * k_int - 1), 4))
    else:
        print(max(4, 4 * k_int))
