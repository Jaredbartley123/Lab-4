#lab 3

def isYearLeap(year):
    if year < 1582:
        return False

    elif year % 400 == 0:
        return True

    elif year % 100 == 0:
        return False

    elif year % 4 == 0:
        return True

    else:
        return False

def daysInMonth(year, month):
    
    leap = isYearLeap(year)

    if leap and month == 2:
        return 29

    elif month == 2:
        return 28

    elif month == 4 or month ==  6 or month == 9 or month == 11:
        return 30

    else:
        return 31


def dayOfYear(year, month, day):

    dayInYear = 0

    for days in range (month - 1):
        dayInYear += daysInMonth(year, days+1)
   
    dayInYear += day

    return(dayInYear)
        


print(dayOfYear(2000, 12, 31))
