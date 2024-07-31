t = int(input())

for _ in range(t):
    n = int(input())

    print("Pairs for " + str(n) + ": ", end="")

    flag = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if(i+j == n):
                if(flag == 1):
                    print(", ", end="")
                print(str(i) + " " + str(j), end="")
                flag = 1
    print()