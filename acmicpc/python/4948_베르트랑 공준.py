
prime_list = list()

prime_check = [0] * 123457*2

for i in range (2, 123457*2):
    if prime_check[i] == 0:
        prime_list.append(i)
        for j in range(i, 123457*2, i):
            prime_check[j] = 1


while True:
    cnt = 0
    n = int(input())
    if(n == 0):
        break

    for item in prime_list:
        if n < item <= 2*n:
            cnt += 1
        elif item > 2*n:
            break
    print(cnt)

