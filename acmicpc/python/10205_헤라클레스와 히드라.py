n = int(input())

for idx in range(n):
    k = int(input())
    arr = list(input())

    for item in arr:
        if item == 'c':
            k += 1
        else:
            k -= 1

    print("Data Set", str(idx + 1) + ":")
    print(k)
    print()
