n = int(input())

prime = list()

for i in range(1, 1000+1):
    if i == 1 or i == 2:
        prime.append(i)
    else:
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break

        if flag == False:
            prime.append(i)

print(n)

for i in range(1, n):
    print(i, end=" ")

print(prime[n])