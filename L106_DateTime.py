from datetime import datetime

mydatetime = datetime(2019, 10, 30, 10, 15, 16)
print(mydatetime)
print(mydatetime.year)
print(mydatetime.second)

newdatetime = mydatetime.replace(year=2023, second=20)
print(newdatetime)
print(newdatetime.year)
print(newdatetime.second)

#Arithmetics on Dates
from datetime import date
print("***** Arithmetics on Dates *****")
date1 = date(2025, 11, 3)
date2 = date(2020, 10, 20)
print(date1 - date2)
result = date1 - date2
print(type(result))
print(result)
print(result.days)

print("***** Arithmetics on Dates *****")
datetime1 = datetime(2025, 11, 3, 22, 10)
datetime2 = datetime(2020, 10, 20, 15, 56)
print(datetime1 - datetime2)
result = datetime1 - datetime2
print(type(result))
print(result)
print(result.days)
print(result.seconds)