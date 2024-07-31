t = int(input())

for p in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1,n-1):
        s = 0
        a[i] = min((a[i-1]+a[i+1]) / 2, a[i])
    print("Case #"+str(p)+":", format(a[n-2], ".6f"))
print()