n = int(input())

while n % 10 == 0:
    n //= 10
print(n)
n = str(n)

print(n.count('0'))