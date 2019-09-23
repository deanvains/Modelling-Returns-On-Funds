def calcMonths(startYear,year2,startMonth,month2):
    if startMonth <= month2:
        return int((year2 - startYear) * 12 + abs((month2-startMonth)))
    else:  
        return int((year2 - startYear - 1) * 12 + abs((12-startMonth+month2)))