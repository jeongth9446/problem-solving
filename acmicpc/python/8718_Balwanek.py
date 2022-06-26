x, k = list(map(int, input().split()))

if int((k + k * 2 + k * 4)*1000) <= x*1000:
    print(int((k + k * 2 + k * 4) * 1000))
elif int((k + k * 0.5 + k * 2)*1000) <= x*1000:
    print(int((k + k * 0.5 + k * 2) * 1000))
elif int((k + k * 0.5 + k * 0.25)*1000) <= x*1000:
    print(int((k + k * 0.5 + k * 0.25) * 1000))
else:
    print(0)