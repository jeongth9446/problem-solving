n = 0

while True:
    try:
        k = input()
        n += 1
    except EOFError:
        break

print(n)
