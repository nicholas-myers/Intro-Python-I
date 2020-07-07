"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

print(sys.argv)

today = datetime.today()
this_year = today.year
this_month = today.month

if len(sys.argv) == 1:
    print(calendar.month(this_year, this_month))
elif len(sys.argv) == 2:
    month = int(sys.argv[1])
    if month > 12 or month < 1:
        print("please enter a valid month 1-12")
    elif month <=12 and month >= 1:
          print(calendar.month(this_year, month))
elif len(sys.argv) == 3:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    if month > 12 or month < 1 or year < 1800:
        print("please enter a valid month 1-12 and year greater than 1800")
    elif month <=12 and month >= 1:
          print(calendar.month(year, month))


# year_month = input("Enter a month: ,Then you may enter a year separated by a comma: ").split(",")
# print(year_month)

# print(sys.argv)
# if year_month == [""]:
#     print(calendar.month(2020, 7))
# elif len(year_month) == 1:
#     month = int(year_month[0])
#     print(calendar.month(2020, month))
# elif len(year_month) > 1:
#     month = int(year_month[0])
#     year = int(year_month[1])
#     if year < 1800 or month > 12:
#         print("Please enter month first then year")
#     else: 
#         print(calendar.month(year, month))

