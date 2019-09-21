from calculations.calcMonth import calcMonths


def calcSpending(spendingAmounts, spendingMonths, spendingYears,startMonth,startYear):
    monthDict = {"January" : 1,
                 "February" : 2,
                 "March" : 3,
                 "April" : 4,
                 "May" : 5,
                 "June" : 6,
                 "July" : 7,
                 "August" : 8,
                 "September" : 9,
                 "October" : 10,
                 "November" : 11,
                 "December" : 12}

    startingMonth = monthDict.get(startMonth)
    startingYear = int(startYear)
    spendingMonths = spendingMonths.split(" ")
    spendingYears = spendingYears.split(" ")
    spendingAmount = spendingAmounts.split(" ")
    months = []
    if len(spendingMonths) != len (spendingYears) or len(spendingAmount) != len(spendingMonths)/2 or len(spendingMonths) % 2 != 0:
        print('fail')

    for i in range(0,len(spendingMonths),2):
        months.append(calcMonths(startingYear,int(spendingYears[i]),startingMonth,monthDict.get(spendingMonths[i])))
        months.append(calcMonths(startingYear,int(spendingYears[i+1]),startingMonth,monthDict.get(spendingMonths[i+1])))


    spending = {}
    i = months[0]
    monthIndex = 0
    spendingIndex = 0
    while i != months[-1]:
        spending[i] = int(spendingAmount[spendingIndex])
        if i == months[monthIndex+1]:
            monthIndex += 2
            spendingIndex += 1
            i = months[monthIndex]
        else:
            i += 1
    spending[months[-1]] = int(spendingAmount[-1])
    print (spending)
    return spending
        