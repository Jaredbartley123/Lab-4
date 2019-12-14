#lab 2

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


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
