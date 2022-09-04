n, k = list(map(int, input().split()))

a = list(map(int, input().split(",")))

# print(a)

for i in range(k):
    for idx in range(n-i-1):
        a[idx] = a[idx+1] - a[idx]

for idx in range(n-k):
    if idx == n-k-1:
        print(a[idx])
    else:
        print(a[idx], end=",")
