t = int(input())

for _ in range(t):
    k = int(input())
    t1 = list(str(k))
    t2 = list(str(k * k))
    if t1 == t2[len(t2) - len(t1):]:
        print("YES")
    else:
        print("NO")
