import datetime
import jdatetime
import os
os.system("cls" if os.name == "nt" else "clear")


print("Please enter your desired 'DateTime' in the format shown: '%Y-%m-%d %H:%M'")
datetime1 = datetime.datetime.strptime(input("DateTime 1: "), "%Y-%m-%d %H:%M")
datetime2 = datetime.datetime.strptime(input("DateTime 2: "), "%Y-%m-%d %H:%M")

diff = abs(datetime1 - datetime2)

# Leap Year: ]f the number is evenly divisible by 4. Confirm the number isn't evenly divisible by 100.
# Check if the number is evenly divisible by 400. If a year is divisible by 100, but not 400, then it
# is not a leap year. Formula:    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) -> True
leap_year = lambda year: (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
count_leap_year = 0

if datetime1.year < datetime2.year:
    for year in range(datetime1.year, datetime2.year):
        if leap_year(year):
            count_leap_year += 1
else:
    for year in range(datetime2.year, datetime1.year):
        if leap_year(year):
            count_leap_year += 1

jdatetime1 = jdatetime.datetime.fromgregorian(datetime=datetime1)
jdatetime2 = jdatetime.datetime.fromgregorian(datetime=datetime2)

print()
print("Time difference in seconds: ", diff.seconds)
print("Leap years betweeb two date:", count_leap_year)
print()
print("DateTime 1 to Jalali:", jdatetime1)
print("DateTime 2 to Jalali:", jdatetime2)
