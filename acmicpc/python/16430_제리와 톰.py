A, B = list(map(int, input().split()))

C, D = B - A, B

for i in range(2, 10):
    # print(i)
    while C % i == 0 and D % i == 0:
        C, D = C // i, D // i

print(C, D)
