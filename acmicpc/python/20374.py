
res = 0
while True:
    try:
        n = float(input())

        res += n
    except EOFError:
        break


print("{:.2f}".format(res))
