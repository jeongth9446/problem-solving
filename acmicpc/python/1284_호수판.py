
arr = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]

while True:
    t = list(input().strip())
    if "".join(t) == '0':
        exit()
    res = 1
    for item in t:
        res += arr[int(item)] + 1

    print(res)
