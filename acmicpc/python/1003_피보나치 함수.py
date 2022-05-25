t = int(input())

fibonacci0 = []
fibonacci1 = []
for i in range(0, 41):
    if i == 0:
        fibonacci0.append(1)
        fibonacci1.append(0)
    elif i == 1:
        fibonacci0.append(0)
        fibonacci1.append(1)
    else:
        fibonacci0.append(fibonacci0[i - 1] + fibonacci0[i - 2])
        fibonacci1.append(fibonacci1[i - 1] + fibonacci1[i - 2])

for t in range(0, t):
    n = int(input())
    print(fibonacci0[n], fibonacci1[n])
