t = int(input())


def f(v: []):
    p = 1
    r = 0
    for i in range(0, 8):
        if v[7 - i] == "I":
            r += p
        p *= 2
    return r


for k in range(1, t + 1):
    n = int(input())
    s = input()
    res = ""
    print("Case #" + str(k) + ": ", end="")
    for i in range(0, n * 8, 8):
        print(chr(f(s[i: i + 8])), end="")
    print()
