n = list(input())

while True:
    if n == list(str(int(n[0])*len(n))):
        print("FA")
        break
    else:
        print(int(n[0]) * len(n))
        n = list(str(int(n[0])*len(n)))
