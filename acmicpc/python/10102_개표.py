n = input()

k = list(input())

A = 0
B = 0

for item in k:
    if item == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")