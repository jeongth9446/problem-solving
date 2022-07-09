a, b, c, d = list(map(int, input().split()))
p, m, n = list(map(int, input().split()))

p1, m1, n1 = p % (a + b), m % (a + b), n % (a + b)
p2, m2, n2 = p % (c + d), m % (c + d), n % (c + d)

resp, resm, resn = 0, 0, 0
if p1 <= a and p1 != 0:
    resp += 1
if p2 <= c and p2 != 0:
    resp += 1

if m1 <= a and m1 != 0:
    resm += 1
if m2 <= c and m2 != 0:
    resm += 1
if n1 <= a and n1 != 0:
    resn += 1
if n2 <= c and n2 != 0:
    resn += 1
# print(p1, m1, n1)
# print(p2, m2, n2)
print(resp)
print(resm)
print(resn)
