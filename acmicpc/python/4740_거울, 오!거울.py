
while True:
    s = input()
    if s == "***":
        break
    s = "".join(reversed(list(s)))
    print(s)
