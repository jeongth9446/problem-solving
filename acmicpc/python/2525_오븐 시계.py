hour, minute = input().split()
remained_minute = input()

hour = int(hour)
minute = int(minute)
remained_minute = int(remained_minute)

calc_hour = int(remained_minute / 60)
calc_minute = remained_minute % 60

minute += calc_minute
if minute >= 60:
    hour += 1
    minute %= 60
hour += calc_hour
if hour >= 24:
    hour %= 24

print(hour, minute)