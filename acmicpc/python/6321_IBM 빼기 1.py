n = int(input())

for k in range(1, n + 1):
    s = list(input().strip())
    s = list(map(lambda x: chr((ord(x) + 1 - ord('A')) % 26 + ord('A')), s))

    print("String #" + str(k))
    print("".join(s))
    print()
 