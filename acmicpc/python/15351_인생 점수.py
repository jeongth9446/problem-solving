n = int(input())

for _ in range(n):
    s = list(input())
    r = 0

    for item in s:
        if item != ' ':
            k = ord(item) - ord('A') + 1
            r += k
    if r == 100:
        print("PERFECT LIFE")
    else:
        print(r)

