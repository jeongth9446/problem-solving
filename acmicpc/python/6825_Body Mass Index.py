weight = float(input())
height = float(input())

res = weight / (height * height)

if res > 25:
    print("Overweight")
elif res < 18.5:
    print("Underweight")
else:
    print("Normal weight")
