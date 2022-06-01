hour, minute = input().split()
hour = int(hour)
minute = int(minute)

if minute >= 45:
    minute -= 45
else:
    if hour > 0:
        hour -= 1
        minute = minute - 45 + 60
    else:
        hour = 23
        minute = minute - 45 + 60

print(hour, minute)
