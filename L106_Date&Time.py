import datetime
mytime1 = datetime.time(2, 20)
mytime2 = datetime.time(13, 54, 23, 28)

print(mytime1.hour)
print(mytime1.minute)
print(mytime1.second)
print(mytime1.microsecond)
print(f"The time is {mytime1}")
print(type(mytime1))

print(mytime2.hour)
print(mytime2.minute)
print(mytime2.second)
print(mytime2.microsecond)
print(f"The time is {mytime2}")

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())

dob = datetime.date(1999, 6, 2)
print(dob)