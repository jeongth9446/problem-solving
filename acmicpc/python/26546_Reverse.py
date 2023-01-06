n = int(input())

for _ in range(n):
    s, a, b = list(map(str, input().split()))
    a = int(a)
    b = int(b)
    s = list(s)

    # print(s, a, b)

    for idx in range(len(s)):
        if a <= idx < b:
            pass
        else:
            print(s[idx], end="")
    print()