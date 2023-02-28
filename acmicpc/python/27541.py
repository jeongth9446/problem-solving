a = input()
b = list(input())

if b[len(b) - 1] == 'G':
    print("".join(b[:-1]))
else:
    print("".join(b) + "G")
