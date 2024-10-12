mat = ['a', 'e', 'i', 'o', 'u']
while True:
    a = input()

    if a == "#":
        break

    cnt = 0

    while a[0] not in mat and cnt != len(a):
        a = a[1:] + a[0]
        cnt += 1

    print(a + "ay")
