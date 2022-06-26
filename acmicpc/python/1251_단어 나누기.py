
t = list(input())

res = ""

for i in range(1, len(t)-1):
    for j in range(i+1, len(t)):
        a = t[0:i]
        b = t[i:j]
        c = t[j:]
        k = "".join(reversed(a)) + "".join(reversed(b)) + "".join(reversed(c))
        # print(a, b, c, k)
        if res == "":
            res = k
        elif res > k:
            res = k

print(res)
