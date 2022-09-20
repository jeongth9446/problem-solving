a = int(input())
b = input()
c = list(map(int, list(b)))
c.reverse()

for i in c:
    print(a * i)
print(a * int(b))
