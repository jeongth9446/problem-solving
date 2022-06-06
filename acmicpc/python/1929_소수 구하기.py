
prime_list = list()

prime_check = [0] * 1000000

for i in range (2, 1000000):
    if prime_check[i] == 0:
        prime_list.append(i)
        for j in range(i, 1000000, i):
            prime_check[j] = 1

m, n = map(int, input().split())

for item in prime_list:
    if m <= item <= n:
        print(item)

