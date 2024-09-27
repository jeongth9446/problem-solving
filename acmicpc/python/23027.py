a = input()

if a.count("A") != 0:
    a = a.replace("B", "A")
    a = a.replace("C", "A")
    a = a.replace("D", "A")
    a = a.replace("F", "A")
elif a.count("B") != 0:
    a = a.replace("C", "B")
    a = a.replace("D", "B")
    a = a.replace("F", "B")
elif a.count("C") != 0:
    a = a.replace("D", "C")
    a = a.replace("F", "C")
else:
    a = "".join(["A" for _ in range(len(a))])

print(a)
