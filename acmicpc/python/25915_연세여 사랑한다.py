c = input()

res = 84

if c > 'I':
    res += ord(c) - 73
else:
    res += 73 - ord(c)
print(res)
