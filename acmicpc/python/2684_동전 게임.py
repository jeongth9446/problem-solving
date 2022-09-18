n = int(input())

for _ in range(n):
    k = list(input())
    res = [0 for i in range(8)]
    for idx in range(38):
        if k[idx] == "T" and k[idx + 1] == "T" and k[idx + 2] == "T":
            res[0] += 1
        if k[idx] == "T" and k[idx + 1] == "T" and k[idx + 2] == "H":
            res[1] += 1
        if k[idx] == "T" and k[idx + 1] == "H" and k[idx + 2] == "T":
            res[2] += 1
        if k[idx] == "T" and k[idx + 1] == "H" and k[idx + 2] == "H":
            res[3] += 1
        if k[idx] == "H" and k[idx + 1] == "T" and k[idx + 2] == "T":
            res[4] += 1
        if k[idx] == "H" and k[idx + 1] == "T" and k[idx + 2] == "H":
            res[5] += 1
        if k[idx] == "H" and k[idx + 1] == "H" and k[idx + 2] == "T":
            res[6] += 1
        if k[idx] == "H" and k[idx + 1] == "H" and k[idx + 2] == "H":
            res[7] += 1

    for r in res:
        print(r, end=" ")
    print()
