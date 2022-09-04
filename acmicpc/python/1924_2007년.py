days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = list(map(int, input().split()))
print(weekday[sum(days_of_month[1:x], y) % 7])
