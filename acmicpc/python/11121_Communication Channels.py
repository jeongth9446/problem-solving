n = int(input())

for _ in range(n):
    a, b = list(map(str, input().split()))

    a = list(a)
    b = list(b)

    if len(a) != len(b):
        print("ERROR")
    else:
        flag = 0
        for idx in range(len(a)):
            if a[idx] != b[idx]:
                flag = 1

        if flag == 0:
            print("OK")
        else:
            print("ERROR")
