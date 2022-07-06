

n, k = list(map(int, input().split()))

y = list()

for i in range(1, n+1):
    if n % i == 0:
        y.append(i)

# print(y)
if len(y) < k:
    print("0")
else:
    print(y[k-1])