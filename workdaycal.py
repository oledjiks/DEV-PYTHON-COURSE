import calendar
d = calendar.Calendar()
workday = 0
for i in range(1, 13):
    for day in d.itermonthdays2(2017, i):
        if day[0] == 0 or day[1] == 5 or day[1] == 6:
            continue
        else:
            workday += 1
print('Количество рабочих дней в 2017 году = ', workday)