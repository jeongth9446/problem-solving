a = int(input())
b = int(input())

res = (a + b) % 12

if res == 0:
    print(12)
else:
    print(res)