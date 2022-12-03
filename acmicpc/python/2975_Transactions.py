while True:
    a = list(map(str, input().split()))
    if a == ['0', 'W', '0']:
        break
    elif "W" in a:
        b = int(a[0]) - int(a[2])
        if b < -200:
            print("Not allowed")
        else:
            print(b)
    elif "D" in a:
        print(int(a[0]) + int(a[2]))
