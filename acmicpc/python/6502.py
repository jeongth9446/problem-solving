t = 1
while True:
    try:
        r, w, l = list(map(int, input().split()))
    except:
        break

    d = (w / 2) * (w / 2) + (l / 2) * (l / 2)
    if r ** 2 >= d:
        print(f"Pizza {t} fits on the table.")
    else:
        print(f"Pizza {t} does not fit on the table.")
    t += 1
