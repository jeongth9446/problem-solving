n = int(input())

for _ in range(n):
    k, a, b, c = list(map(int, input().split()))

    print(str(k) + " " + str(a + b + c), end=" ")
    if a / 35 >= 0.3 and b / 25 >= 0.3 and c / 40 >= 0.3 and a + b + c >= 50:
        print("PASS")
    else:
        print("FAIL")
       