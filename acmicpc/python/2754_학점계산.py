grade = input()

if grade == 'F':
    print("0.0")
    exit(0)

base = 0.0

if grade[0] == 'A':
    base = 4.0
elif grade[0] == 'B':
    base = 3.0
elif grade[0] == 'C':
    base = 2.0
elif grade[0] == 'D':
    base = 1.0

if grade[1] == '+':
    base += 0.3
elif grade[1] == '-':
    base -= 0.3

print(base)
