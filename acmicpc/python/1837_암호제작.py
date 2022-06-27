p, k = list(map(int, input().split()))


for i in range(2, 1000000+1):
    if p % i == 0 and i < k:
        print("BAD "+str(i))
        exit()

print("GOOD")