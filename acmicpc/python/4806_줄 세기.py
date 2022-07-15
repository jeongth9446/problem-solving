import sys

res = 0

while True:
    try:
        s = input()
        res += 1
    except EOFError:
        break

print(res)