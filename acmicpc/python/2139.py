import datetime

while True:
    day, month, year = map(int, input().split())

    if day == month == year == 0:
        break

    inputDay = datetime.datetime(year=year, month=month, day=day)
    defaultDay = datetime.datetime(year=year, month=1, day=1)

    gap = inputDay - defaultDay

    print(gap.days + 1)
