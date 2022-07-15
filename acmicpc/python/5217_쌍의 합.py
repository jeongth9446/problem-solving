t = int(input())

for _ in range(t):
    n = int(input())

    print("Pairs for " + str(n) + ":", end="")
    cnt = 0
    for k in range(1, int(n/2)+1):
        if n - k > k:
            cnt += 1
            if cnt == 1:
                print(" " + str(k) + " " + str(n-k), end="")
            else:
                print(", " + str(k) + " " + str(n-k), end="")

    print()
