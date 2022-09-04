
while True:
    try:
        k = input()
        while k != k.replace('BUG', ''):
            k = k.replace('BUG', '')
        print(k)
    except EOFError:
        break

