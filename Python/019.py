import datetime

myDate = datetime.datetime(1901, 1, 1)

counter = 0
while myDate.year != 2001:
    if myDate.day == 1:
        # print(myDate)
        counter += 1
    myDate += datetime.timedelta(days=7)

print(counter)
