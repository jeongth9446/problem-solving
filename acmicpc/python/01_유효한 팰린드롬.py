a = input()
b = list()

for ch in a:
    if ch.isalnum():
        b.append(ch.capitalize())

while len(b) > 1:
    if b.pop(0) != b.pop():
        print("False")

print("True")