n = int(input())

for i in range(1, 1000000):
    t = map(int, list(str(i)))
    sum = i
    for k in t:
        sum += k
    if sum == n:
        print(i)
        exit()

print(0)
