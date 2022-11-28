while True:
    a, b = list(map(int, input().split()))
    if a == b == 0:
        break

    # print(2*a-b, 2*b-a, (a+b)/2)

    if (a + b) / 2 == (a + b) // 2:
        print(min(2 * a - b, 2 * b - a, (a + b) // 2))
    else:
        print(min(2 * a - b, 2 * b - a))
  