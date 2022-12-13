n = int(input())

for _ in range(n):
    k = list(map(int, input().split()))
    print("Denominations: ", end="")
    for item in k[1:]:
        print(item, end=" ")
    print()
    flag = True

    for i in range(1, k[0]):
        if k[i] * 2 > k[i+1]:
            flag = False
    if flag:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()

