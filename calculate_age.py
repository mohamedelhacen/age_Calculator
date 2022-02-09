import time
from calendar import isleap

# Check the leap year
def if_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

# Get the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

age = input("Enter your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

end_year = int(localtime.tm_year)
begin_year = end_year - year

# Get number of days
for y in range(begin_year, end_year):
    if (if_leap_year(y)):
        day += 366
    else:
        day += 365

leap_year = if_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day += month_days(m, leap_year)

day += localtime.tm_mday

print("You age is ", year, " years or", end=" ")
print(month, "months or ",day, "days")