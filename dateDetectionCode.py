# Program that can detect dates in the DD/MM/YYYY format.
# e.g: 29/11/2020 which is today xD
# Assume the days range(01,31), months is range(01,12) and years range(1000,2999). If the day or month is a single digit it needs a leading 0 like 04 for April
# Detect if its a valid date. April, June, September and November = 30 days and the rest have 30 days. February has 28 days in normal years and 29 days in leap years
# Leap years are every year evenly divisible by 4, except for years evenly divisble by 100, unless the year is also evenly divisible by 400. < This almost bugged my head but I think I've made it work in the end

import re

# Regex to detect DD/MM/YYYY
dateRegex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9]{3})')
mo = dateRegex.search('29/11/2020')

if mo == None:
    print('Date not found')
# Variables
day = mo.group(1)
month = mo.group(2)
year = mo.group(3)
leap = year
# Checking for leap year:
if int(year) % 4 == 0:
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            year = leap
            print('it is a leap year')
        else:
            year = year
            print('it is not a leap year')
    else:
        year = leap
        print('it is a leap year')
else:
    year = year
    print('it is not a leap year')



# Printing the date:
if mo != None:
    print('Date found: ' + mo.group())

# Checking if it is a valid date:
if month == '04' or '06' or '09' or '11':
    if day >= '31':
        print('Incorrect date. This month can have only 30 days at max.')
#Changing the value of February to have max 29 days if it is a leap year:
if month == '02':
    if year == leap:
        if int(day) > 29:
            print('Sorry but February cant have more than 29 days in a leap year.')
