n = int(input())

s = list()
s.append("")

for _ in range(n):
    s.append(input())

m = int(input())

for _ in range(m):
    t = int(input())

    print("Rule " + str(t) + ": ", end="")

    if t <= 0 or t > n:
        print("No such rule")
    else:
        print(s[t])
