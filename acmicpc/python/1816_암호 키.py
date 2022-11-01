# 1816 암호 키

N = 1_000_000

# Make Prime Set
prime = list()

chk = [0 for _ in range(N)]

for i in range(2, N):
    if chk[i] == 0:
        prime.append(i)
        for k in range(i, N, i):
            chk[k] = 1

# print(len(prime))

# Input
n = int(input())

# Process
for _ in range(n):
    k = int(input())
    flag = True
    for item in prime:
        if k % item == 0:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
