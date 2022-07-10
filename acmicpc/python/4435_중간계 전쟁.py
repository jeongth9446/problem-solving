t = int(input())

for k in range(t):
    a = sum(list(map(lambda x, y: x*y, list(map(int, input().split())), [1, 2, 3, 3, 4, 10])))
    b = sum(list(map(lambda x, y: x * y, list(map(int, input().split())), [1, 2, 2, 2, 3, 5, 10])))

    if a < b:
        s = "Evil eradicates all trace of Good"
    elif a > b:
        s = "Good triumphs over Evil"
    else:
        s = "No victor on this battle field"

    print("Battle " + str(k+1) + ": " + s)

