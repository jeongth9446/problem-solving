n = int(input())

for _ in range(n):
    res = 0
    tot_len = 0
    while True:
        t = list(input())
        if len(t) == 0:
            break
        tot_len += len(t)
        for item in t:
            if item == '#':
                res += 1
    # print((tot_len-res)/tot_len*100)

    pres = "{0:0.1f}".format((tot_len - res) / tot_len * 100)
    pres = pres.replace(".0", "")

    print("Efficiency ratio is " + pres + "%.")
