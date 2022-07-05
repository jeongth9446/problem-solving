b1 = list(map(int, list(input())))
b2 = list(map(int, list(input())))

# print (b1, b2)

k = 1
a1 = a2 = 0
b1.reverse()
b2.reverse()
for i in b1:
    a1 += i * k
    k *= 2

k = 1

for i in b2:
    a2 += i * k
    k *= 2

c1 = a1 * a2

c = list()

while c1 != 0:
    c.append(str(c1 % 2))
    c1 //= 2

c.reverse()

print("".join(c))
