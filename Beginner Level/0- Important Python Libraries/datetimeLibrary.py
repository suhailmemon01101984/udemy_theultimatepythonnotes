'''
datetime


datetime is a library for working with dates and times in Python. 
It provides a range of classes and functions for representing and 
manipulating dates and times, including support for time zones and 
daylight saving time.

Example use case: Calculate the number of days between two dates.

'''

from datetime import date

d1 = date(2021, 1, 1)
d2 = date(2021, 12, 31)

delta = d2 - d1

print(delta.days)

