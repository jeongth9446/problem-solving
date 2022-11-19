n = int(input())

for _ in range(n):
    k = list(map(int, input().split()))
    cnt = 0
    for i in k:
        if i >= 10:
            cnt += 1
        print(i, end=" ")
    print()
    if cnt == 3:
        print("triple-double", end="\n\n")
    elif cnt == 2:
        print("double-double", end="\n\n")
    elif cnt == 1:
        print("double", end="\n\n")
    else:
        print("zilch", end="\n\n")
