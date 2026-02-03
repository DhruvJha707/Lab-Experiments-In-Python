'''Write a program which takes any date as input and display next date of the calendar 
e.g. 
I/P: day=20 month=9 year=2005  
O/P: day=21 month=9 year 2005 '''


# input date
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# days in each month
if month == 2:
    # check leap year
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        max_days = 29
    else:
        max_days = 28
elif month in (1, 3, 5, 7, 8, 10, 12):
    max_days = 31
else:
    max_days = 30

# logic for next date
if day < max_days:
    day = day + 1
else:
    day = 1
    if month < 12:
        month = month + 1
    else:
        month = 1
        year = year + 1

# output
print("Next Date:")
print("day =", day, "month =", month, "year =", year)
