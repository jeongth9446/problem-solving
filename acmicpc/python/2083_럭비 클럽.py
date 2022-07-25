while True:
    a, b, c = list(input().split())

    b = int(b)
    c = int(c)
    
    if a == "#" and b == c == 0:
        break

    print(a, end=" ")
    if b > 17 or c >= 80:
        print("Senior")
    else:
        print("Junior")
