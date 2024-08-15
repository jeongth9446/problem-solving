n = int(input())

a = list(input())
b = list(input())

for i in range(len(a)):
    cnt = 0
    x = 0
    sc = ""
    cur = "R"
    if a[i] == "S":
        cnt += 1
    if b[i] == "S":
        cnt += 1
    if a[i] == "P":
        cnt -= 1
    if b[i] == "P":
        cnt -=1

    if x < cnt:
        x = cnt
        sc = cur

    cnt = 0
    cur = "P"
    if a[i] == "R":
        cnt += 1
    if b[i] == "R":
        cnt += 1
    if a[i] == "S":
        cnt -= 1
    if b[i] == "S":
        cnt -=1

    if x < cnt:
        x = cnt
        sc = cur

    cnt = 0
    cur = "S"
    if a[i] == "P":
        cnt += 1
    if b[i] == "P":
        cnt += 1
    if a[i] == "R":
        cnt -= 1
    if b[i] == "R":
        cnt -=1

    if x < cnt:
        x = cnt
        sc = cur

    print(sc, end="")