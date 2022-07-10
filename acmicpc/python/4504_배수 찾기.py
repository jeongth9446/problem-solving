n = int(input())

while True:
    k = int(input())
    if k == 0:
        break

    if k % n == 0:
        print(str(k) + " is a multiple of " + str(n) + ".")
    else:
        print(str(k) + " is NOT a multiple of " + str(n) + ".")
