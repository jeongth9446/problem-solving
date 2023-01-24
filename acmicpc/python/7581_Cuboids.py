while True:
    l, w, h, v = list(map(int, input().split()))

    if l == w == h == v == 0:
        break

    if l == 0:
        print(v // (w * h), w, h, v)
    elif w == 0:
        print(l, v // (l * h), h, v)
    elif h == 0:
        print(l, w, v // (l * w), v)
    else:
        print(l, w, h, l * w * h)
   