S = input()

for item in S:
    if item.isupper():
        print(item.lower(), end="")
    else:
        print(item.upper(), end="")

print()
