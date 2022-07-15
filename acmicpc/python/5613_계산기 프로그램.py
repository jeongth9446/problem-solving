import sys

input = sys.stdin.readline

k = int(input())
while True:
    b = input().strip()
    if b == '=':
        print(k)
        break
    else:
        a = int(input())
        if b == '+':
            k += a
        elif b == '-':
            k -= a
        elif b == '/':
            k = int(k/a)
        elif b == '*':
            k *= a