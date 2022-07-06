tt = int(input())

for i in range(tt):
    n = int(input())

    res = 0
    for k in range(1, n+1):
        res += k*int((k+2)*(k+1)/2)

    print(res)

