def checkPrime(v):
    for i in range(2, v):
        if v % i == 0:
            return False
    return True


k = list(input())

s = 0
for item in k:
    if ord('A') <= ord(item) <= ord('Z'):
        s += ord(item) - ord('A') + 1 + 26
    elif ord('a') <= ord(item) <= ord('z'):
        s += ord(item) - ord('a') + 1

# print(s)
if checkPrime(s):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
