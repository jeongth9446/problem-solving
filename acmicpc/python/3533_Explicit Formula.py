x = list(map(int, input().split()))

res = 0

for i in range(10):
    for j in range(i+1, 10):
        if x[i] == 1 or x[j] == 1:
            res += 1

for i in range(10):
    for j in range(i+1, 10):
        for k in range(j+1, 10):
            if x[i] == 1 or x[j] == 1 or x[k] == 1:
                res += 1

if res % 2 == 0:
    print(0)
else:
    print(1)
