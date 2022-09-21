n = list(map(int, input().split()))

flag = True

while flag:
    flag = False

    for idx in range(len(n) - 1):
        if n[idx] > n[idx + 1]:
            n[idx], n[idx + 1] = n[idx + 1], n[idx]
            for item in n:
                print(item, end=" ")
            print()
            flag = True
