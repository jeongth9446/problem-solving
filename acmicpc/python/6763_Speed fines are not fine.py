
lim = int(input())
item = int(input())
res = 0

if lim + 1 <= item <= lim + 20:
    res += 100
elif lim + 21 <= item <= lim + 30:
    res += 270
elif item >= lim + 31:
    res += 500

if res == 0:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is $" + str(res) + ".")
